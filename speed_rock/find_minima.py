# find_minima.py
import numpy as np
import time
import tracemalloc
from speed_rock import load_h5_data

def find_minima(rcdata: np.ndarray, benchmark: bool = True) -> np.ndarray:
    """
    Identify local minima in the rocking curve data.

    Parameters
    ----------
    benchmark : bool, optional
        If True, prints runtime and peak memory usage.

    Returns
    -------
    np.ndarray
        Array labelling the rocking curve.
    """
    if benchmark:
        start_time = time.perf_counter()
        tracemalloc.start()

    

    center = rcdata[:, 1:-1]
    mask = center < rcdata[:, :-2]
    mask &= center < rcdata[:, 2:]
    mask &= center > 740
    mask = mask.astype(np.uint8)
    np.cumsum(mask, axis=1, out=mask)
    mask = np.pad(mask, ((0, 0), (1, 1)), mode='edge')
    mask += 1

    if benchmark:
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        elapsed = time.perf_counter() - start_time
        print(f"Runtime: {elapsed:.6f} s")
        print(f"Peak memory: {peak / 1e6:.3f} MB")

    return mask
