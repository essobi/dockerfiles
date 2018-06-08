FROM debian:latest  
MAINTAINER Mongo <willem@xcloudbiz.com>  
  
RUN apt-get update \  
&& apt-get -y install wget \  
&& cd /usr \  
&& wget http://www.linuxdot.net/down/jexus-5.8.2-x64.tar.gz \  
&& tar -zxvf jexus-5.8.2-x64.tar.gz \  
&& apt-get -y autoremove --purge wget \  
&& rm -rf /var/lib/apt/lists/* jexus-5.8.2-x64.tar.gz  
  
EXPOSE 80  
WORKDIR /usr/jexus  
CMD /usr/jexus/jwss  

