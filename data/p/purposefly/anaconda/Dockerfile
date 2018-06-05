FROM debian:jessie  
  
MAINTAINER tomas.bouda@purposefly.com  
  
# environment fix  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
## install packages  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update --fix-missing \  
&& apt-get install -y \  
wget \  
bzip2 \  
ca-certificates \  
libglib2.0-0 \  
libxext6 \  
libsm6 \  
libxrender1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
## Anaconda3 installation  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh \  
&& wget --quiet
https://repo.continuum.io/archive/Anaconda3-4.3.0-Linux-x86_64.sh \  
&& /bin/bash /Anaconda3-4.3.0-Linux-x86_64.sh -b -p /opt/conda \  
&& rm /Anaconda3-4.3.0-Linux-x86_64.sh  
  
ENV PATH=/opt/conda/bin:$PATH  

