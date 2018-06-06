FROM ubuntu:14.04  
MAINTAINER Thach Mai <contact@thachmai.info>  
  
  
##############  
# Add the mono xamarin key and repository  
RUN apt-get update -q  
RUN apt-get -y -q install wget  
RUN wget http://download.mono-project.com/repo/xamarin.gpg  
RUN apt-key add xamarin.gpg  
RUN rm xamarin.gpg  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get update -q  
  
##############  
# Install mono-complete package  
RUN apt-get -y -q install mono-complete  
  

