# docker friendly ubuntu 14.04 base image -
https://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:0.9.11  
MAINTAINER Thorben Stangenberg <thorben@stangenberg.net>  
  
# Set correct environment variables.  
ENV HOME /root  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Ensure we create the cluster with UTF-8 locale  
RUN locale-gen en_US.UTF-8 && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# add webupt8 repository - see http://www.webupd8.org/  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update && apt-get -y upgrade  
  
# automatically accept oracle license  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# install java 7 oracle jdk  
RUN apt-get -y install oracle-java7-installer  
RUN update-alternatives --display java  
  
# configure JAVA_HOME  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> /etc/environment  
  
# Clean up when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

