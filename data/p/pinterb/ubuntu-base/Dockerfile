# pinterb/ubuntu-base  
#  
# VERSION 0.0.13  
#  
# CREATED ON 2015-02-19T17:28:53UTC  
  
FROM ubuntu:14.04  
  
MAINTAINER Brad Pinter brad.pinter@gmail.com  
  
ENV HOME /root  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
ENV DEBIAN_FRONTEND noninteractive  
  
### apt update, upgrade and install base packages  
RUN apt-get update -q && \  
apt-get -y upgrade && \  
apt-get install -y \  
build-essential \  
software-properties-common \  
language-pack-en \  
socat \  
python-software-properties python-setuptools python-pip python-all-dev \  
byobu curl htop unzip vim wget rsync tree less \  
locales daemontools cron \  
git mercurial bzr subversion  
  
# Create a generic "build" directory  
RUN mkdir /build/  
  
## Put watcherf in $PATH  
ADD http://dl.bintray.com/pinterb/watchf/linux/watchf_x86_64.tar.gz
/usr/local/bin/  
RUN cd /usr/local/bin && \  
tar -xvf watchf_x86_64.tar.gz && \  
chmod +x watchf && \  
rm watchf_x86_64.tar.gz  
  
### create a user for whatever application we choose to run.  
# DOCKER BUG RUN addgroup --gid 9999 app && \  
# alias adduser='useradd' && \  
# adduser --uid 9999 --gid 9999 --disabled-password --gecos "Application" app
&& \  
# usermod -L app && \  
# mkdir -p /home/app/.ssh && \  
# mkdir -p /home/app/bin && \  
# chmod 700 /home/app/.ssh && \  
# chown app:app /home/app/.ssh && \  
# chown app:app /home/app/bin  
  
### create a user for logging.  
# DOCKER BUG RUN addgroup --gid 9998 log && \  
# adduser --uid 9998 --gid 9998 --disabled-password --no-create-home --gecos
"Logger" log && \  
# usermod -L log  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
# This is probably a Docker bug.  
# DOCKER BUG RUN mkdir /var/shared/ && \  
# touch /var/shared/placeholder && \  
# chown -R app:app /var/shared  
  
#VOLUME /var/shared  
  
### make debian interactive...  
RUN env --unset=DEBIAN_FRONTEND  
  
### define default command.  
CMD ["/bin/bash"]  

