# This is the docker file to setup a webmin server to administer bind. One
would expect that you  
# would install the bind9 package in here, but doing so results in an error.
This build requires  
# that the user manually install the bind module through webmin once the
container has started  
FROM ubuntu:12.04  
MAINTAINER Programster  
  
# We need to ensure the universe repo is used in order to get libauthen-pam-
perl later  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >>
/etc/apt/sources.list  
  
RUN apt-get update  
  
# Install the packages webmin relies upon  
RUN apt-get install python perl libnet-ssleay-perl openssl libauthen-pam-perl
libio-pty-perl apt-show-versions -y  
  
# Add the webmin package  
ADD webmin_1.660_all.deb /root/webmin_1.660_all.deb  
  
# Install webmin using gdebi which will auto install dependencies  
RUN dpkg -i /root/webmin_1.660_all.deb  
  
# expose port 8080 so that our webserver can respond to requests.  
EXPOSE 10000

