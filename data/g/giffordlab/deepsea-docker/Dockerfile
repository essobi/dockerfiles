FROM kaixhin/cuda-torch:7.0  
MAINTAINER Matt Edwards <matted@mit.edu>  
  
RUN apt-get update  
RUN apt-get update && apt-get install -y \  
curl \  
emacs24-nox \  
gcc-4.8-plugin-dev \  
libhdf5-dev \  
luarocks \  
libmatio2 \  
nano \  
pkg-config  
  
# Get required Lua packages.  
RUN /root/torch/install/bin/luarocks install cutorch  
RUN /root/torch/install/bin/luarocks install cunn  
RUN /root/torch/install/bin/luarocks install matio  
RUN /root/torch/install/bin/luarocks install hdf5  
# RUN /root/torch/install/bin/luarocks install mattorch # No MATLAB in the
container.  
# Bring DeepSEA source code into the image.  
RUN mkdir /root/deepsea  
COPY *.lua /root/deepsea/  
  
# Bring DeepSEA example data into the image (can be replaced with docker run
-v).  
RUN mkdir /root/deepsea/input  
COPY *.mat /root/deepsea/input/  
  
WORKDIR /root/deepsea  
  
CMD /root/torch/install/bin/th main.lua -save results -verbose  

