FROM debian:stable  
  
MAINTAINER Leonard Marschke <leonard@marschke.me>  
  
# update software repos  
RUN apt-get update \  
# upgrade software  
&& apt-get -y upgrade \  
&& apt-get -y install apt-utils \  
# install inkscape and some needed fonts  
&& apt-get -y install \  
inkscape \  
fonts-liberation fonts-font-awesome \  
# clean up  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

