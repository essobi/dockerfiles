FROM ichizero/cuda-opencv:latest  
  
LABEL maintainer="ichizero"  
  
RUN apt update && \  
apt install -y x11-apps && \  
apt clean  
  
RUN pip3 install --no-cache-dir \  
chainer \  
hdf5storage \  
h5py \  
scipy \  
py3nvml \  
cython \  
argparse \  
matplotlib  

