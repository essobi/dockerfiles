FROM kaixhin/torch:latest  
  
RUN apt-get install -y git  
#RUN apt-get install -y wget  
RUN apt-get install -y libprotobuf-dev  
RUN apt-get install -y protobuf-compiler  
RUN apt-get install -y libhdf5-serial-dev  
RUN apt-get install -y hdf5-tools  
RUN apt-get install -y python-setuptools  
RUN apt-get install -y python-dev  
  
RUN cd / ; git clone https://github.com/karpathy/neuraltalk2.git  
RUN luarocks install loadcaffe  
#here CUDA toolkit is not intalled since I don't have a GPU to test it on, see
this Dockerfile for examples
https://hub.docker.com/r/halo9pan/cuda/~/dockerfile/  
#RUN luarocks install cutorch  
RUN cd / ; git clone https://github.com/deepmind/torch-hdf5.git  
RUN cd /torch-hdf5/ && luarocks make hdf5-0-0.rockspec
LIBHDF5_LIBDIR="/usr/lib/x86_64-linux-gnu/"  
RUN easy_install pip && pip install h5py  
RUN curl https://deb.nodesource.com/setup_5.x|sh -  
RUN apt-get install -y nodejs  
ADD webapp /webapp  
ADD README.md /webapp/README.md  
RUN cd /webapp && /usr/bin/npm install  
CMD ["/usr/bin/node","/webapp/index.js"]  
WORKDIR /webapp  

