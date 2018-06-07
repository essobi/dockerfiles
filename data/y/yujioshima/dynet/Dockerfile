FROM yujioshima/dynet:base-in-python  
  
# DyNet, version 4234759  
ENV DYNET_VERSION 4234759  
RUN cd /opt && \  
git clone https://github.com/clab/dynet.git && \  
cd dynet && \  
git checkout ${DYNET_VERSION} && \  
mkdir build && \  
cd build && \  
cmake .. -DEIGEN3_INCLUDE_DIR=/opt/eigen -DPYTHON=`which python` && \  
make -j2 && \  
cd python && \  
python setup.py install  
ENV DYLD_LIBRARY_PATH /opt/dynet/build/dynet/:$DYLD_LIBRARY_PATH  
WORKDIR /opt/dynet  

