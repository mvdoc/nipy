__docformat__ = 'restructuredtext'

from neuroimaging import traits

from neuroimaging.defines import pylab_def
PYLAB_DEF, pylab = pylab_def()

# Interpolation schemes

if PYLAB_DEF:

    interpolation = traits.Trait('bilinear', 'nearest', 'blackman100',
                                 'blackman256', 'blackman64',
                                 'sinc144', 'sinc256', 'sinc64', 'bicubic',
                                 'spline16', 'spline36')

    # Color mappings available

    _names = dir(pylab.cm)
    _cmdict = {}
    for _name in _names:
        try:
            exec('_cm = pylab.cm.%s' % _name)
            if type(_cm) == type(pylab.cm.hot):
                _cmdict[_name] = _cm
        except:
            pass


    _cmapn = _cmdict.keys()
    _cmapn.pop(_cmapn.index('spectral'))
    _cmapn = ['spectral'] + _cmapn
    _cmapn = tuple(_cmapn)
    cmap = traits.Trait(*_cmapn, **{'desc':'A pylab colormap.'})

    def getcmap(cmapname):
        return _cmdict[cmapname]
