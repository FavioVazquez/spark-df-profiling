import os

__location__ = os.path.dirname(__file__)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='spark-df-profiling-optimus',
    version='0.1.1',
    author='Favio Vazquez - Julio Antonio Soto de Vicente',
    author_email='favio.vazquez@ironmussa.com',
    packages=['spark_df_profiling_optimus'],
    url='https://github.com/FavioVazquez/spark-df-profiling-optimus',
    download_url='https://github.com/FavioVazquez/spark-df-profiling-optimus/archive/0.1.1.tar.gz',
    license='MIT',
    description='Create HTML profiling reports from Apache Spark DataFrames',
    install_requires=[
        "pandas>=0.17.0",
        "matplotlib>=2.0",
        "jinja2>=2.8",
        "six>=1.9.0"
    ],
    include_package_data = True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Framework :: IPython',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'

    ],
    keywords='spark pyspark report big-data pandas data-science data-analysis python jupyter ipython',

)
