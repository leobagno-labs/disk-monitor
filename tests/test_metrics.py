# Writing tests for metrics functions
import pytest
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

def test_used_percent():
    """Test the used_percent function with edge cases."""
    assert used_percent(50, 100) == 100.0
    assert used_percent(0, 100) == 0.0
    assert used_percent(100, 100) == 100.0
    assert used_percent(75, -5) == 0.0
    assert used_percent(30, 0) == 0.0

def test_bytes_to_gib():
    """Test byte conversion to GiB."""
    assert bytes_to_gib(1073741824) == 1.0  
    assert bytes_to_gib(5368709120) == 5.0  
    assert bytes_to_gib(0) == 0.0
    assert bytes_to_gib(2147483648) == 2.0
    assert bytes_to_gib(1024 ** 3) == 1.0

def test_format_disk_summary():
    """ Verify formatting includes key metrics. """
    stats=DiskStats(total=1024**3, used=512*(1024**2), free=512*(1024**2))
    summary = format_disk_summary(stats)
    assert "Total: 1.00 GiB" in summary
    assert "Used: 0.50 GiB" in summary
    assert "Free: 0.50 GiB" in summary
    assert "50" in summary
   

def test_diskstats_immutable():
    """ Ensure DiskStats is immutable. """
    stats = DiskStats(total=1000, used=500, free=500)
    with pytest.raises(AttributeError):
        stats.used = 999 # pyright: ignore

def test_format_memory_summary():
    """ Verify formatting includes key metrics. """
    stats=MemoryStats(total=8589934592, available=4294967296, percent= 50.0)
    summary = format_memory_summary(stats)
    assert "Total" in summary
    assert "Available" in summary
    assert "50.0%" in summary

    