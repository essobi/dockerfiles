# Pull base image.  
FROM ubuntu:trusty  
  
MAINTAINER Tristan Salles  
  
RUN apt-get update -y  
  
RUN apt-get install -y git python-pip python-dev libzmq3 libzmq3-dev pkg-
config libfreetype6-dev libpng3 libopenmpi-dev openmpi-bin libhdf5-dev
liblapack-dev llvm-3.6 libedit-dev gfortran  
  
RUN pip install -U setuptools  
RUN pip install -U pip # fixes AssertionError in Ubuntu pip  
RUN pip install enum34  
RUN LLVM_CONFIG=llvm-config-3.6 pip install llvmlite==0.8.0  
RUN pip install jupyter markupsafe zmq singledispatch backports_abc certifi
jsonschema ipyparallel path.py matplotlib mpi4py==1.3.1
git+https://github.com/badlands-model/triangle pandas plotly  
RUN apt-get install -y libnetcdf-dev python-mpltoolkits.basemap  
RUN pip install Cython==0.20  
RUN pip install h5py  
RUN pip install scipy  
RUN pip install numpy  
RUN pip install numba==0.23.1 ez_setup  
RUN pip install gFlex  
RUN pip install netcdf4  
RUN pip install colorlover  
RUN pip install cmocean  
RUN pip install scikit-fuzzy  
RUN pip install pyevtk  
  
ENV TINI_VERSION v0.8.4  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/local/bin/tini  
RUN chmod +x /usr/local/bin/tini  
  
RUN mkdir /workspace  
  
#RUN mkdir /workspace && \  
# mkdir /workspace/volume  
# setup space for working in  
# VOLUME /workspace/volume  
# launch notebook  
WORKDIR /workspace  
RUN git clone https://github.com/tristan-salles/PoC.git  
  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
# ENV
LD_LIBRARY_PATH=/workspace/volume/pyBadlands/pyBadlands/libUtils:/build/pyBadlands/pyBadlands/libUtils  
CMD jupyter notebook --ip=0.0.0.0 --no-browser \  
\--NotebookApp.token='' \--allow-root
--NotebookApp.iopub_data_rate_limit=1.0e10  

