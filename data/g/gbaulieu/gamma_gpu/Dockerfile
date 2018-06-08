FROM ubuntu:latest  
MAINTAINER Guillaume Baulieu <g.baulieu@ipnl.in2p3.fr>  
RUN apt-get update && apt-get install -y git dpkg-dev cmake g++ gcc binutils
libx11-dev libxpm-dev libxft-dev libxext-dev gfortran libssl-dev libpcre3-dev
xlibmesa-glu-dev libglew1.5-dev libftgl-dev libmysqlclient-dev libfftw3-dev
graphviz-dev libavahi-compat-libdnssd-dev libldap2-dev python-dev libxml2-dev
libkrb5-dev libgsl0-dev libqt4-dev wget libboost-all-dev libeigen3-dev python-
setuptools vim unzip subversion emacs autoconf automake libtool graphviz gv
libunwind8 libunwind-dev libtinyxml-dev  
ADD known_hosts /root/.ssh/known_hosts  
ADD cuda-repo-ubuntu1604_8.0.61-1_amd64.deb /opt/cuda-repo-
ubuntu1604_8.0.61-1_amd64.deb  
RUN dpkg -i /opt/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb && apt-get update &&
DEBIAN_FRONTEND=noninteractive apt-get install -y cuda-8.0  
RUN cd /opt/ && wget
ftp://lyoftp.in2p3.fr/baulieu/libcudnn6_6.0.21-1+cuda8.0_amd64.deb && dpkg -i
/opt/libcudnn6_6.0.21-1+cuda8.0_amd64.deb && rm
/opt/libcudnn6_6.0.21-1+cuda8.0_amd64.deb  
RUN cd /opt/ && wget https://root.cern.ch/download/root_v6.12.04.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz && tar -xzf root_v6.12.04.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz && rm root_v6.12.04.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz  
RUN cd /opt/ && wget ftp://lyoftp.in2p3.fr/baulieu/tensorflow_gpu_ubuntu16.tgz
&& tar -xzf tensorflow_gpu_ubuntu16.tgz && rm tensorflow_gpu_ubuntu16.tgz &&
touch /bin/nvidia-smi  

