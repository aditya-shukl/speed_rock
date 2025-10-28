# load_data.py
import os
import h5py
import numpy as np

def load_h5_data(filepath="./assets/example_data/data.h5"):
    """
    Load rocking curve data from an HDF5 file.

    Parameters
    ----------
    file_path : str, optional
        Path to the HDF5 file containing the data.

    Returns
    -------
    np.ndarray
        The 'rocking_curves' dataset.
    """
    datapath = os.path.join(file_path)
    with h5py.File(datapath, 'r') as hin:
        rcdata = hin['rocking_curves'][()]
    return rcdata
