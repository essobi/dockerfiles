FROM frankhinek/datascience  
  
LABEL maintainer="Frank Hinek <frank.hinek@gmail.com>"  
  
# Install TensorFlow Dependencies  
# Based on
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/Dockerfile  
RUN apt-get -qq update && apt-get -qq -y install --no-install-recommends \  
build-essential \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
rsync \  
software-properties-common \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Custom binary C++ based protobuf pip package  
ENV
protobuf_url=https://storage.googleapis.com/tensorflow/linux/cpu/protobuf-3.1.0-cp35-none-
linux_x86_64.whl  
  
ARG tensorflow_version=1.4.1  
ENV
tf_binary_url=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${tensorflow_version}-cp35-cp35m-linux_x86_64.whl  
  
# Install Protobuf and TensorFlow CPU version from central repo  
RUN pip --no-cache-dir install \  
${protobuf_url} \  
${tf_binary_url}  
  
# TensorBoard  
EXPOSE 6006  

