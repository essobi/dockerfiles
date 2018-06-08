FROM ubuntu:16.04  
MAINTAINER Masaki Muranaka <monaka@monami-ya.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install unzip sudo git subversion openjdk-8-jre-headless  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN apt-get -y install software-properties-common && \  
add-apt-repository -y ppa:team-gcc-arm-embedded/ppa && \  
apt-get -y remove software-properties-common  
  
RUN apt-get -y update  
RUN apt-get -y install build-essential gcc-arm-none-eabi=15:4.9.3+svn231177-1
u-boot-tools libboost1.58-all-dev  
RUN apt-get -y autoremove && apt-get -y autoclean  
  
WORKDIR /projects  
EXPOSE 22 4401 4403  
CMD tail -f /dev/null  

