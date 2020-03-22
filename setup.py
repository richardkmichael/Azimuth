# from Cython.Build import cythonize
from setuptools import setup


setup(name='Azimuth',
      version='2.0',
      author='Nicolo Fusi and Jennifer Listgarten',
      author_email="fusi@microsoft.com, jennl@microsoft.com",
      description=("Machine Learning-Based Predictive Modelling of CRISPR/Cas9 guide efficiency"),
      packages=["azimuth", "azimuth.features", "azimuth.models", "azimuth.tests"],
      package_data={'azimuth': ['saved_models/*.*']},
      install_requires=['scipy==1.2.1',
                        'numpy==1.14.5',
                        'matplotlib==2.2.4',
                        'nose',
                        'scikit-learn>=0.17.1,<0.18',
                        'pandas==0.19.2',
                        'biopython',
                        'xlrd>=1.0.0'],
      license="BSD",
      # ext_modules=cythonize("ssk_cython.pyx"),
      )
