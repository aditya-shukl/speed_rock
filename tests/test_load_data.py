# tests/test_load_data.py
import h5py
import numpy as np
from speed_rock.load_data import load_h5_data

def test_load_h5_data(tmp_path):
    # Create a temporary HDF5 file
    file_path = "./test_data.h5"
    data = np.random.rand(10, 10)
    with h5py.File(file_path, 'w') as f:
        f.create_dataset('rocking_curves', data=data)

    # Run the loader
    loaded = load_h5_data(filepath="./test_data.h5")

    # Verify
    assert isinstance(loaded, np.ndarray)
    assert loaded.shape == data.shape
    np.testing.assert_allclose(loaded, data)
