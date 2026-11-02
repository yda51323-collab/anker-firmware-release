#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""固件版本号解析与发布批次校验。"""
import sys

VENDOR = "安克创新"
QUARTERS = ("2026Q3", "2026Q4")


def parse(version):
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        raise ValueError("bad version: %s" % version)
    return tuple(int(p) for p in parts)


def sort_key(version):
    return parse(version)


def check_batch(batch):
    if batch not in QUARTERS:
        raise ValueError("unknown batch: %s" % batch)
    return batch


def main(version, expect):
    v = parse(version)
    check_batch(expect)
    print("vendor=%s version=%d.%d.%d batch=%s" % ((VENDOR,) + v + (expect,)))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("usage: fw_version.py <version> --expect <batch>")
        sys.exit(1)
    sys.exit(main(sys.argv[1], sys.argv[3]))
