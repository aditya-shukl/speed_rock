import numpy as np
from speed_rock import find_minima

def test_find_minima():
    print("Running test_find_minima...")

    rc = np.array([
        [700, 750, 720, 710, 730],
        [800, 780, 770, 760, 750],
    ], dtype=np.uint16)

    mask = find_minima(rc)

    assert isinstance(mask, np.ndarray)
    assert mask.shape[0] == rc.shape[0]
    assert np.all(mask >= 1)
    assert mask[4] == 2  # Check known minima position

    print("Passed: find_minima produces valid output")

if __name__ == "__main__":
    test_find_minima()
