FROM debian:jessie  
MAINTAINER Oliver Lade <oliver.lade@unimelb.edu.au>  
  
  
# Install g++ and dependencies to build the converter.  
RUN apt-get update && apt-get -qq install git make cmake g++ libxml2-dev
libpng12-dev libpcre3-dev pkg-config  
  
# Build and install the converter.  
RUN git clone \--recurse-submodules https://github.com/KhronosGroup/glTF.git  
RUN cd /glTF/converter/COLLADA2GLTF && cmake . && make  
RUN ln -s /glTF/converter/COLLADA2GLTF/bin/collada2gltf /usr/local/bin/  
  
# Create a working directory to mount.  
VOLUME ["/data"]  
WORKDIR /data  
ENTRYPOINT ["collada2gltf"]  
  

