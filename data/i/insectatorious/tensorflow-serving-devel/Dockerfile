FROM ubuntu:18.04  
MAINTAINER Sumanas Sarma <insectatorious+docker@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
libcurl3-dev \  
git \  
libfreetype6-dev \  
libpng-dev \  
libzmq3-dev \  
pkg-config \  
python-dev \  
python-numpy \  
python-pip \  
software-properties-common \  
swig \  
zip \  
zlib1g-dev  
  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-
apt stable tensorflow-model-server tensorflow-model-server-universal" | tee
/etc/apt/sources.list.d/tensorflow-serving.list  
  
RUN curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-
serving.release.pub.gpg | apt-key add -  
  
RUN apt-get update && apt-get install tensorflow-model-server  
  
ENTRYPOINT ["tensorflow_model_server"]  

