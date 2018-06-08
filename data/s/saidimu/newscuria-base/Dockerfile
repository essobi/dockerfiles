############################################################  
# base Dockerfile for newscuria services  
############################################################  
FROM ubuntu:trusty  
  
# Dockerfile author/maintainer  
MAINTAINER Saidimu Apale (saidimu@gmail.com)  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
# set up timezone  
RUN echo 'America/Montreal' > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# Workaround for https://github.com/docker/docker/issues/6345  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
## 1. Add PPA repo key  
## 2. Accept Oracle Java license  
## 3. Add Oracle JRE sources  
## 4. Update sources  
## 5. Upgrade packages  
## 6. Install new packages  
## 7. Add NodeJS sources  
## 8. Update sources  
## 9. Install Node JS  
## 10. Clean up APT.  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list.d/webupd8.list && \  
apt-get -qq update > /dev/null && \  
apt-get -yqq upgrade > /dev/null && \  
apt-get -yqq install vim.tiny wget zip unzip build-essential curl software-
properties-common scons oracle-java7-set-default nodejs > /dev/null && \  
apt-add-repository -y ppa:chris-lea/node.js > /dev/null && \  
apt-get -qq update > /dev/null && \  
apt-get -yqq install nodejs > /dev/null && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD [""]

