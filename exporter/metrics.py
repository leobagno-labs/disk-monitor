# System metrics library- v1.0

from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class DiskStats:
    total: int
    used: int
    free: int

@dataclass(frozen=True)
class MemoryStats:
    total: int
    available: int
    percent: float


def clamp(value: int, min_value: int, max_value: int) -> int:
    # Clamp function to be within [min_value, max_value]
    return max(min_value, min(value, max_value))

def used_percent(total: int, used: int) -> float:
    if total <= 0:
        return 0.0
    used_clamped = clamp(used, 0, total)
    return (used_clamped / total) * 100
   
def bytes_to_gib(bytes_value: int) -> float:
     # Convert bytes to gigabytes
    return bytes_value / (1024 ** 3)

    # Format bytes to human-readable string

def format_disk_summary(stats: DiskStats) -> str:
    pct= used_percent(stats.total, stats.used)
    return(
        f"Disk Summary: Total: {bytes_to_gib(stats.total):.2f} GiB, "
        f"Used: {bytes_to_gib(stats.used):.2f} GiB ({pct:.2f}%), "
        f"Free: {bytes_to_gib(stats.free):.2f} GiB"
    )

def format_memory_summary(stats: MemoryStats) -> str:

    return(
        f"Memory Summary: Total: {bytes_to_gib(stats.total):.2f} GiB, "
        f"Available: {bytes_to_gib(stats.available):.2f} GiB ({stats.percent:.2f}%)"
        f"Used: {stats.percent:.1f}%"
    )
    
    