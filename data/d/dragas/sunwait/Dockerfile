FROM debian:stretch  
MAINTAINER Stefano Marinelli <stefano@dragas.it>  
  
RUN apt-get update; apt-get -y install wget g++ make; \  
mkdir /tmp/sunwait; cd /tmp/sunwait; wget
https://sourceforge.net/projects/sunwait4windows/files/sunwait0-8.tar/download
-O sunwait.tar; tar xf sunwait.tar; cd sunwait/0.8/; make; cp sunwait
/usr/local/bin; cd /tmp/; rm -Rf sunwait; \  
apt-get -y remove wget g++ make; apt-get -y autoremove; apt-get clean; rm -rf
/var/lib/apt/lists/*  

