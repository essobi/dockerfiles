FROM ubuntu:17.04  
MAINTAINER Hugo Josefson <hugo@josefson.org>  
  
RUN echo Packages last updated 2016-11-19.  
  
RUN apt-get update && apt-get install -y aptitude && aptitude dist-upgrade
--purge-unused -y && aptitude clean  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y sudo ubuntu-gnome-
desktop  

