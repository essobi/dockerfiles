FROM debian:latest  
MAINTAINER Antonio Xanxess <dr.ignoto@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
RUN echo "locales locales/locales_to_be_generated multiselect es_ES.UTF-8
UTF-8" | debconf-set-selections &&\  
echo "locales locales/default_environment_locale select es_ES.UTF-8" |
debconf-set-selections  
  
RUN apt-get install -y locales wget  
  
ENV LC_ALL es_ES.UTF-8  
RUN apt-get install -y subversion vim openssh-client  

