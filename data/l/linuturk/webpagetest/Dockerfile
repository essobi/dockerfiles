FROM ubuntu:14.04  
MAINTAINER Justin Phelps <linuturk@onitato.com>  
  
# Set various options  
USER root  
WORKDIR /root  
  
# Update OS  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Fix locale  
RUN locale-gen en_US.UTF-8  
  
# Web Page Test Tasks go here  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository -y ppa:mc3man/trusty-media  
RUN apt-get update  
RUN apt-get install -y apache2 php5 imagemagick libimage-exiftool-perl
libjpeg-turbo-progs ffmpeg php5-curl php5-gd php5-sqlite php5-apcu  

