# load_data.py
import os
import h5py
import numpy as np

def load_h5_data(filepath):
    """
    Load rocking curve data from an HDF5 file.

    Parameters
    ----------
    file_path : str
        Path to the HDF5 file containing the data.

    Returns
    -------
    np.ndarray
        rocking curves numpy array.
    """
    with h5py.File(filepath, 'r') as hin:
        rcdata = hin['rocking_curves'][()]
    return rcdata
