# based on hwuethrich/bamboo-server  
# Bamboo Server  
#  
# VERSION 0.0.1  
FROM phusion/baseimage:0.9.19  
MAINTAINER Lukas Hetzenecker  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Environment  
ENV BAMBOO_VERSION 5.7.2  
ENV BAMBOO_HOME /home/bamboo  
  
# Expose web and agent ports  
EXPOSE 8085  
EXPOSE 54663  
# Add runit service  
ADD bamboo-server.sh /etc/service/bamboo-server/run  
  
ADD bamboo.cfg.xml.new /etc/bamboo.cfg.xml.new  
  
# Prepare repos for Oracle Java 7 and Docker  
RUN apt-get install -yq software-properties-common && add-apt-repository
ppa:webupd8team/java -y  
RUN apt-get install -yq apt-transport-https  
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN sh -c "echo deb https://apt.dockerproject.org/repo ubuntu-xenial main >
/etc/apt/sources.list.d/docker.list"  
RUN apt-get update && apt-get upgrade -y  
  
# Install Oracle Java 7  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -yq oracle-java8-installer  
  
# PostgreSQL Client  
RUN apt-get install -yq postgresql-client  
  
# VCS tools  
RUN apt-get install -yq git subversion  
  
# Docker  
RUN apt-get install -yq docker-engine  
  
# docker-compose  
RUN apt-get install -yq python-pip  
RUN pip install docker-compose  
  
# XML Parser  
RUN apt-get install -yq xmlstarlet  
  

