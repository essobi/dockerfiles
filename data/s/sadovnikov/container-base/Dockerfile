FROM debian:jessie  
MAINTAINER Viktor Sadovnikov <viktor@jv-ration.com>  
  
RUN apt-get update  
RUN apt-get -qqy install \  
openjdk-7-jdk \  
sudo \  
tar \  
unzip \  
wget \  
&& apt-get clean  
  
ADD envvars.sh /etc/profile.d/envvars.sh  

