FROM nvidia/cuda:8.0-cudnn5-devel  
  
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>  
# Update CA Certificates  
RUN apt-get update && \  
apt-get install -y \--reinstall \  
ca-certificates && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
  
# Python 2  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends \  
python-dev && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
# pip  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
WORKDIR "/root"  
CMD ["/bin/bash"]  

