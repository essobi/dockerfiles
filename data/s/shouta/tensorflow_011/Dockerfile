FROM nvidia/cuda:8.0-cudnn5-devel  
  
MAINTAINER Shota Onishi <s-onishi@dts.co.jp>  
  
RUN sudo apt-get -y update  
RUN sudo apt-get -y upgrade  
RUN sudo DEBIAN_FRONTEND=noninteractive apt-get -y install build-essential git
python-pip libfreetype6-dev libxft-dev libncurses-dev libopenblas-dev gfortran
python-matplotlib libblas-dev liblapack-dev libatlas-base-dev python-dev
python-pydot linux-headers-generic linux-image-extra-virtual unzip python-
numpy swig python-pandas python-sklearn unzip wget pkg-config zip g++
zlib1g-dev libcurl3-dev  
RUN sudo pip install -U pip  
  
RUN sudo apt-get -y install software-properties-common python-software-
properties  
RUN sudo add-apt-repository -y ppa:webupd8team/java  
RUN sudo apt-get -y update  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-
set-selections  
RUN sudo apt-get -y install -y oracle-java8-installer  
  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list  
RUN curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | sudo
apt-key add -  
RUN sudo apt-get -y update  
RUN sudo apt-get -y install bazel  
RUN sudo apt-get -y upgrade bazel  
  
RUN sudo pip install --upgrade
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0-cp27-none-
linux_x86_64.whl  
  
WORKDIR /root  
RUN git clone https://github.com/tensorflow/models.git  
  
WORKDIR /root/models/inception/  
RUN bazel build inception/imagenet_train  
RUN bazel build inception/imagenet_eval  
RUN bazel build inception/build_image_data  
  
EXPOSE 10080  
CMD /bin/bash  

