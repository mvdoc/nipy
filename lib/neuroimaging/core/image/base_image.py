class BaseImage(object):
    """
    This class define a minimal interface which different types of images
    should implement. This interface is used by the Image class, which is
    the class which should be used by applications.
    """

    def __init__(self, data, grid, sctype):
        self.grid = grid
        self.data = data
        self.sctype = sctype
        
    def __getitem__(self, item):
        return self.data[item]
        
    def __setitem__(self, item, value):
        self.data[item] = value

class ArrayImage (BaseImage):
    """A simple class to mimic an image file from an array."""
    def __init__(self, data, grid=None):
        """
        Create an ArrayImage instance from an array,
        by default assumed to be 3d.

        >>> from numpy import *
        >>> from neuroimaging.core.image import Image
        >>> z = Image.ArrayImage(zeros((10,20,20)))
        >>> print z.ndim
        3
        """
        grid = grid and grid or SamplingGrid.identity(self.shape)
        sctype = data.dtype.type
        BaseImage.__init__(self, data, grid, sctype)
