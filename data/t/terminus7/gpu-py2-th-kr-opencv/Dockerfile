FROM terminus7/gpu-py2-th-kr  
  
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>  
  
ARG CUDA_ARCHITECTURE="3.0"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
python-opencv \  
libdc1394-22-dev \  
libopencv-dev \  
libtbb2 \  
libtbb-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libv4l-dev \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH}  
ENV LIBRARY_PATH /usr/lib/x86_64-linux-gnu:${LIBRARY_PATH}  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

