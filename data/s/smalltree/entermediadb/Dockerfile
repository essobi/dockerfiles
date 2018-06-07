FROM ubuntu:14.04  
MAINTAINER Keri Alleyne <info@symlogix.com>  
RUN apt-get update && apt-get install -y \  
nano \  
software-properties-common \  
wget  
RUN add-apt-repository universe  
RUN add-apt-repository multiverse  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN add-apt-repository "deb http://packages.entermediadb.org/repo/apt stable
main"  
RUN wget -O /etc/apt/trusted.gpg.d/entermediadb.gpg
http://packages.entermediadb.org/repo/apt/entermediadb.gpg  
RUN apt-get update && apt-get install -y \  
entermediadb  

