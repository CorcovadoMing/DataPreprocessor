import datum_pb2
import numpy as np

def datum_to_array(datum):
    """Converts a datum to an array. Note that the label is not returned,
    as one can easily get it by calling datum.label.
    """
    if len(datum.data):
        return np.fromstring(datum.data, dtype=np.uint8).reshape(
            datum.height, datum.width, datum.channels)
    else:
        return np.array(datum.float_data).astype(float).reshape(
            datum.height, datum.width, datum.channels)

def array_to_datum(arr, label=None):
    """Converts a 3-dimensional array to datum. If the array has dtype uint8,
    the output data will be encoded as a string. Otherwise, the output data
    will be stored in float format.
    """
    if arr.ndim != 3:
        raise ValueError('Incorrect array shape.')
    datum = datum_pb2.Datum()
    datum.height, datum.width, datum.channels = arr.shape
    if arr.dtype == np.uint8:
        datum.data = arr.tostring()
    else:
        datum.float_data.extend(arr.astype(float).flat)
    if label is not None:
        datum.label = label
    return datum
