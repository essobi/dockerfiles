FROM debian:stretch  
  
MAINTAINER Jaroslaw Filiochowski <jarfil@gmail.com>  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
salt-common && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  

