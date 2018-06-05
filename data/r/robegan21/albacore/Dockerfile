FROM ubuntu:16.04  
LABEL Maintainer="Rob Egan<RSEgan@lbl.gov>"  
  
WORKDIR /root  
  
ARG WHL=ont_albacore-2.1.10-cp35-cp35m-manylinux1_x86_64.whl  
  
ENV WHL_URL https://mirror.oxfordnanoportal.com/software/analysis/${WHL}  
  
# This is necessary because the upgrade sometimes prompts for input  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y strace wget python3-setuptools python3-pip \  
python3-h5py python3-numpy python3-dateutil python3-progressbar \  
libboost-filesystem1.58.0 libboost-program-options1.58.0 \  
libboost-system1.58.0 libboost-log1.58.0 libboost-thread1.58.0 \  
libboost-python1.58.0 && \  
( [ -f ${WHL} ] || wget $WHL_URL ) && \  
pip3 install ${WHL} && \  
rm *.whl && \  
apt-get remove -y wget && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* && \  
find / -name '*.pyc' -exec rm {} \;  
  
CMD ["read_fast5_basecaller.py", "-h"]  
  

