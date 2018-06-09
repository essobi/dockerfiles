# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
# Based on https://hub.docker.com/r/evarga/jenkins-slave/  
FROM ubuntu:trusty  
MAINTAINER Reinout van Rees <reinout@vanrees.org>  
  
# Install and configure a basic SSH server  
RUN apt-get update &&\  
apt-get install -y openssh-server &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/* &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Install JDK 7 (latest edition)  
RUN apt-get update &&\  
apt-get install -y openjdk-7-jdk &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
  
# Set user jenkins to the image  
RUN adduser --quiet jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Extra N&S stuff  
RUN apt-get update &&\  
apt-get install -y \  
build-essential \  
curl \  
gettext \  
git \  
libevent-dev \  
libncurses-dev \  
libreadline-dev \  
lynx-cur \  
memcached \  
nginx \  
python-dev \  
python-gdal \  
python-imaging \  
python-lxml \  
python-mapnik \  
python-matplotlib \  
python-nose \  
python-pandas \  
python-pil \  
python-psycopg2 \  
python-scipy \  
python-tornado \  
unzip &&\  
apt-get clean -y && rm -rf /var/lib/apt/lists/*  
  
# Standard SSH port  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]

