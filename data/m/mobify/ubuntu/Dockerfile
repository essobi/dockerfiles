FROM ubuntu:15.10  
MAINTAINER Mobify <ops@mobify.com>  
  
RUN apt-get -qq update && \  
apt-get -q -y upgrade && \  
apt-get install -y sudo curl wget locales && \  
apt-get remove --purge -y $(apt-mark showauto) && \  
rm -rf /var/lib/apt/lists/*  
  
# Ensure that we always use UTF-8 and with Canadian English locale  
RUN locale-gen en_CA.UTF-8  
  
COPY ./default_locale /etc/default/locale  
RUN chmod 0755 /etc/default/locale  
  
ENV LC_ALL=en_CA.UTF-8  
ENV LANG=en_CA.UTF-8  
ENV LANGUAGE=en_CA.UTF-8  

