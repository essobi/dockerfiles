FROM ubuntu:trusty  
  
MAINTAINER Ian Howson  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main restricted universe
multiverse" > /etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list  
RUN echo "deb http://security.ubuntu.com/ubuntu trusty-security main
restricted universe multiverse" >> /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y git python-pip python-dev libzmq3 libzmq3-dev pkg-
config libfreetype6-dev libpng3 libopenmpi-dev openmpi-bin libhdf5-openmpi-dev
liblapack-dev llvm-3.6 libedit-dev gfortran petsc-dev libxml2-dev xorg-dev
curl libpng12-dev libxft-dev xvfb freeglut3 freeglut3-dev libgl1-mesa-dri
libgl1-mesa-glx rsync xauth python-tk swig  
  
RUN pip install -U setuptools  
RUN pip install -U pip # fixes AssertionError in Ubuntu pip  
RUN pip install enum34  
RUN LLVM_CONFIG=llvm-config-3.6 pip install llvmlite==0.8.0  
RUN pip install jupyter markupsafe zmq singledispatch backports_abc certifi
jsonschema ipyparallel path.py matplotlib mpi4py
git+https://github.com/badlands-model/triangle pandas plotly pyvirtualdisplay  
RUN apt-get install -y libnetcdf-dev python-mpltoolkits.basemap  
RUN pip install Cython==0.20 h5py scipy numpy  
RUN pip install numba==0.23.1 ez_setup  
RUN pip install gFlex netcdf4 colorlover pyevtk  
  
# Clean APT cache to save space in the final image  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

