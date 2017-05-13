FROM python:3.4
MAINTAINER Tobias Kölling <tobias.koelling@physik.uni-muenchen.de>
RUN apt-get update && apt-get -y install \
    liblapack-dev \
    libatlas-dev \
    gfortran \
    libhdf5-dev \
    libnetcdf-dev
RUN pip install --no-cache-dir \
    numpy \
    scipy \
    sympy \
    matplotlib
