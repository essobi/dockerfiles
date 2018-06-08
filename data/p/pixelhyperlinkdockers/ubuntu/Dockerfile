# PixelHyperlink Ubuntu Docker  
#  
# VERSION 1.8.0  
FROM ubuntu:latest  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base Ubuntu Server 16.04 LTS OS."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.8.0"  
LABEL com.pixelhyperlink.docker.ubuntu.version="1.8.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.ubuntu.release-date="2017-07-04"  
LABEL com.pixelhyperlink.docker.ubuntu.version.is-production="true"  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# Expose ssh.  
EXPOSE 22  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Update and Upgrade ubuntu.  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install apt-utils  
RUN apt-get -y install \  
locales \  
tzdata && apt-get -y upgrade  
  
# Set the locale  
RUN locale-gen en_AU en_AU.UTF-8  
ENV LANG en_AU.UTF-8  
ENV LANGUAGE en_AU:en  
ENV LC_ALL en_AU.UTF-8  
#===================  
# Timezone settings  
# Possible alternative:
https://github.com/docker/docker/issues/3359#issuecomment-32150214  
#===================  
ENV AU "AU/Brisbane"  
RUN echo "${AU}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
# Upgrade Distro  
RUN apt-get -y dist-upgrade  
  
# Install essential packages. openssh-server, curl, and lynx-cur are for
debugging the container.  
RUN apt-get install -y \  
ack-grep \  
autoconf \  
aufs-tools \  
automake \  
build-essential \  
bzip2 \  
ca-certificates \  
curl \  
dnsutils \  
dpkg-sig \  
file \  
g++ \  
gcc \  
git \  
imagemagick \  
iputils-ping \  
libcap-dev \  
libsqlite3-dev \  
libtool \  
lsof \  
lynx-cur \  
make \  
net-tools \  
nmap \  
openssh-server \  
patch \  
pkg-config \  
python-software-properties \  
reprepro \  
smartmontools \  
software-properties-common \  
tmux \  
unzip \  
vim \  
wget \  
xz-utils \  
zip && apt-get clean  
  
# Copy SSH config  
COPY ./ssh_config /etc/ssh/ssh_config  
  
# Copy server ssh start up scripts  
COPY ./ssh_startup.sh /opt/ssh_startup.sh  
  
# Run ssh startup scripts  
RUN chmod 755 /opt/ssh_startup.sh  
  
ENTRYPOINT ["/opt/ssh_startup.sh"]  

