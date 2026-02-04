# Writing tests for metrics functions

from exporter.metrics import (
    DiskStats,
    MemoryStats,
    clamp,
    used_percent,
    bytes_to_gib,
    format_disk_summary,
    format_memory_summary,
)

def test_clamp():
    # provide test cases that are prone to breaking
    assert clamp(3, 0, 10) == 3
    assert clamp(-20, 0, 10) == 0
    assert clamp(35, 0, 10) == 10

