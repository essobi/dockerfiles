FROM buildpack-deps:xenial  
MAINTAINER Michael Opitz <michael.opitz@icg.tugraz.at>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
gcc \  
git \  
g++ \  
imagemagick \  
libatlas-dev \  
libatlas-base-dev \  
libboost-all-dev \  
libblas-dev \  
libeigen3-dev \  
liblapack-dev \  
liblas-dev \  
liblas-c-dev \  
libprotobuf-dev \  
libopencv-dev \  
mlocate \  
unzip \  
wget \  
openssh-server \  
puppet \  
sudo \  
wget \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
RUN useradd --create-home --shell /bin/bash vagrant  
RUN echo vagrant:vagrant | chpasswd  
RUN echo root:vagrant | chpasswd  
RUN echo "vagrant ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/01_vagrant &&
chmod 0400 /etc/sudoers.d/01_vagrant  
RUN mkdir /var/run/sshd  
ADD
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub \  
/home/vagrant/.ssh/authorized_keys  
RUN chown -R vagrant:vagrant /home/vagrant/.ssh  
RUN chmod 0600 /home/vagrant/.ssh/authorized_keys  
RUN chmod 0700 /home/vagrant/.ssh  
CMD ["/usr/sbin/sshd", "-D", "-e"]  
EXPOSE 22  

