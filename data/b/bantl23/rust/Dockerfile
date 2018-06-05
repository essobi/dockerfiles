FROM ubuntu:xenial  
  
RUN apt-get update && \  
apt-get install -y \  
wget \  
curl \  
man-db \  
software-properties-common && \  
echo "deb http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee
/etc/apt/sources.list.d/bazel.list && \  
curl https://storage.googleapis.com/bazel-apt/doc/apt-key.pub.gpg | apt-key
add - && \  
apt-get update && \  
apt-get install -y \  
sudo \  
git-core \  
build-essential \  
file \  
default-jdk \  
bazel \  
iputils-ping \  
ssh \  
vim  
  
RUN useradd -m -G sudo docker  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
USER docker  
  
RUN curl https://sh.rustup.rs >> /tmp/rustup  
RUN sh /tmp/rustup -y  
RUN rm /tmp/rustup  
  
CMD ["/bin/bash"]  

