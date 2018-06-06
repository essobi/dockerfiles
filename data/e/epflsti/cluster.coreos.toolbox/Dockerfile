# In case you want quickdev with the toolbox :  
# docker pull epflsti/cluster.coreos.toolbox  
# docker run --privileged -v $PWD:/cwd -it epflsti/cluster.coreos.toolbox
/bin/bash  
FROM ubuntu:xenial  
MAINTAINER STIIT Dev <stiitdev@groupes.epfl.ch>  
  
# Use baseimage-docker's init system.  
# CMD ["/sbin/my_init"]  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Comment "src" sources  
RUN sed -i "s/^deb\\-src/\\#deb\\-src/" /etc/apt/sources.list  
# Use ch mirror  
RUN sed -i "s/archive.ubuntu.com/ch.archive.ubuntu.com/g"
/etc/apt/sources.list  
# and add multiverse package in case we need something else  
RUN apt update && apt install -y software-properties-common curl  
RUN apt-add-repository multiverse  
  
# Ubuntu update + upgrades  
RUN apt -q update && apt -qy upgrade  
  
# Latest node version ('cause you know...)  
# https://by-example.org/install-node-js-5-7-on-ubuntu-16-04-xenial-xerus-lts/  
RUN curl --silent --location https://deb.nodesource.com/setup_5.x | bash -  
  
# Install STIIT tools  
RUN apt install -y --no-install-recommends \  
arping \  
build-essential \  
ca-certificates \  
dmidecode \  
## docker.io \  
emacs \  
ethtool \  
facter \  
file \  
git \  
htop \  
httpry \  
iftop \  
iperf \  
ipmitool \  
iproute2 \  
iputils-ping \  
jq \  
less \  
lsof \  
ltrace \  
man-db \  
manpages \  
mtr \  
net-tools \  
nicstat \  
nmap \  
nodejs \  
openssl \  
psmisc \  
rsync \  
silversearcher-ag \  
sntop \  
smartmontools \  
strace \  
stunnel \  
sysstat \  
telnet \  
tcpdump \  
tcptraceroute \  
telnet \  
vim \  
vnstat \  
wget  
  
COPY docker_script /usr/local/bin/docker  
RUN chmod +x /usr/local/bin/docker  
  
WORKDIR /root/  
COPY bash_profile .bash_profile  
  
COPY motd motd  
RUN chmod +x motd  
  
# Get a "docker" PS1 prompt  
RUN echo 'export "LANG=C.UTF-8"' >> /root/.bashrc  
RUN echo "PS1='⚠ DOCKER! \u@\h:\w\$ '" >> /root/.bashrc  
RUN echo ". motd" >> /root/.bashrc  
  
# Clean up APT when done.  
RUN apt-get clean && apt-get autoremove  
# RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

