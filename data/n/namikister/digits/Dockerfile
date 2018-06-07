FROM namikister/caffe  
LABEL maintainer "Yuta Namiki <namikister@gmail.com>"  
  
ENV DIGITS_VERSION 4.0  
LABEL com.nvidia.digits.version="4.0"  
  
# workaround: gcc and libhdf5-dev are dependencies that are currently missing
from the torch package  
ENV DIGITS_PKG_VERSION 4.0.0-1  
RUN echo "deb http://developer.download.nvidia.com/compute/machine-
learning/repos/ubuntu1404/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list  
RUN apt-get update && apt-get install -y --no-install-recommends \  
torch7-nv=0.9.99-1+cuda7.5 \  
graphviz \  
gcc \  
libhdf5-dev \  
digits=$DIGITS_PKG_VERSION && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /data  
VOLUME /jobs  
  
WORKDIR /usr/share/digits  
  
COPY digits.cfg digits/digits.cfg  
EXPOSE 34448  
ENTRYPOINT ["./digits-server"]  

