from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


ext_modules = cythonize([
    Extension("rect", ['rect.pyx'], 
    libraries=['rectangle'], 
    library_dirs=['rectangle/build'],
    include_dirs=['rectangle'],
    runtime_library_dirs=['rectangle/build'],
    language='c++')
])
setup(name='rect', ext_modules=ext_modules, cmdclass = {'build_ext': build_ext})
