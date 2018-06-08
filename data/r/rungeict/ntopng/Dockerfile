FROM ubuntu:16.04  
MAINTAINER Matthew Mckenzie <mmckenzie@vostronet.com>  
  
RUN apt-get update && apt-get -y -q install wget lsb-release  
RUN wget http://apt-stable.ntop.org/16.04/all/apt-ntop-stable.deb  
RUN dpkg -i apt-ntop-stable.deb && rm -rf apt-ntop-stable.deb  
  
RUN apt-get update  
RUN apt-get -y -q install ntopng ntopng-data  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 3000  
ENTRYPOINT ["ntopng"]  

