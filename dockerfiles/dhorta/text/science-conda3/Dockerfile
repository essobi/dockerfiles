FROM continuumio/miniconda:py34_latest

RUN apt-get update -y
RUN apt-get install --yes build-essential libc6 gfortran g++

RUN conda update -y -q conda
RUN conda install -y -q python=3.4 conda-build setuptools numpy scipy cython numba matplotlib h5py
RUN conda install -y -q pandas scikit-learn
RUN conda install -y -q anaconda-client
RUN conda config --add channels r
RUN conda install r rpy2
RUN apt-get install git -q -y
RUN apt-get install --reinstall gcc gcc-4.7 gcc-4.7-base libgcc1 cpp-4.7 -q -y
RUN conda install -y -q swig
