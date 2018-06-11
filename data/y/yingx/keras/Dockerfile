FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
# Institute of Computer Software, Nanjing University <icsnju@163.com>  
  
ENV APT_INSTALL="apt install -y --no-install-recommends"  
ENV PIP_INSTALL="pip --no-cache-dir install "  
  
RUN apt update && \  
${APT_INSTALL} curl git wget vim unzip python2.7 python-pip python-setuptools
sudo && \  
${PIP_INSTALL} --upgrade pip && \  
${PIP_INSTALL} tensorflow-gpu keras h5py && \  
apt clean ; apt autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* ~/*  

