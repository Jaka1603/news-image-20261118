"""The World in One Day -- entry for the make.fun news-image-20261118 bounty.

The image sums up the world news of Wednesday 18 November 2026, the day
the world's front pages were led by one interlocking set of stories:

  * the United States struck a Revolutionary Guard missile site on
    Iran's Qeshm Island, and Iran answered with drones against a US
    radar site in Bahrain and the Ali Al Salem base in Kuwait;
  * Ukraine hit the Kerch Bridge to Crimea for a second day and a
    road span dropped into the strait;
  * Xi Jinping received Vladimir Putin in Shenzhen for the APEC
    summit week, with a Xi-Trump meeting set for Thursday;
  * the Ebola outbreak in DR Congo more than doubled in three
    months, past 11,000 cases and some 5,400 deaths (UN);
  * the United States lost the measles-elimination status it had
    held for 26 years, with a record 5,400-plus cases (PAHO);
  * Nvidia reported its first quarter since Jensen Huang's exit --
    $115.8 billion of revenue -- and its board refused to bring
    him back.

The finished artwork ships with this repository as ``image.jpg``.
This program checks those bytes against the competition gate
(a whole PNG or JPEG, at most 1 MiB, at most 1024 by 1024 pixels)
and copies them verbatim to ``$MAKEFUN_OUTPUT_DIR/entry.png``
(the grader's default output directory is ``/output``), so every
run writes byte-identical output.  Pure Python 3 standard library;
no network access.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576  # 1 MiB gate limit for the image file
MAX_SIDE = 1024        # gate limit for width and height, in pixels

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def png_size(data):
    """Return (width, height) read from a PNG's IHDR chunk."""
    if data[:8] != PNG_MAGIC or data[12:16] != b"IHDR":
        raise ValueError("not a PNG with an IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def jpeg_size(data):
    """Return (width, height) from the first JPEG SOF0/SOF2 segment."""
    if data[:3] != JPEG_MAGIC:
        raise ValueError("not a JPEG")
    pos = 2
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            raise ValueError("JPEG segment does not start with 0xFF")
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        pos += 2 + length
    raise ValueError("no JPEG SOF segment found")


def image_size(data):
    """Dispatch on the magic bytes: the gate tells PNG and JPEG apart
    by their first bytes, and so does this check."""
    if data[:8] == PNG_MAGIC:
        return png_size(data)
    return jpeg_size(data)


def check_gate(data):
    """Raise ValueError unless the bytes pass the competition gate."""
    if len(data) > MAX_BYTES:
        raise ValueError(f"image is {len(data)} bytes, over the 1 MiB gate")
    width, height = image_size(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError(f"image is {width}x{height}, over the 1024 px gate")
    return width, height


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "image.jpg")

    with open(source_path, "rb") as fh:
        data = fh.read()

    width, height = check_gate(data)
    digest = hashlib.sha256(data).hexdigest()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(data)

    # Read the copy back: the grader runs this program twice and the
    # two outputs must be the same bytes, so prove the write landed
    # exactly rather than assume it.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if hashlib.sha256(written).hexdigest() != digest:
        raise ValueError("the written entry.png does not match the source image")

    print(f"wrote {out_path}: {len(data)} bytes, {width}x{height}, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
