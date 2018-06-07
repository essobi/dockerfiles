FROM terminus7/gpu-py3  
  
MAINTAINER Luis Mesas <luis.mesas@intelygenz.com>  
  
# new system dependencies  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
g++ \  
libblas-dev \  
python3-tk \  
git && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# new python dependencies  
RUN pip --no-cache-dir install \  
matplotlib \  
numpy \  
pandas \  
pillow \  
scikit-image \  
scipy \  
nose \  
sklearn \  
tensorflow-gpu  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

