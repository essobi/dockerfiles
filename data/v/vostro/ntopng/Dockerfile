FROM ubuntu:16.04  
MAINTAINER Matthew Mckenzie <mmckenzie@vostronet.com>  
  
RUN apt-get update && apt-get -y -q install wget lsb-release  
RUN wget http://apt.ntop.org/16.04/all/apt-ntop.deb  
RUN dpkg -i apt-ntop.deb && rm -rf apt-ntop.deb  
  
RUN apt-get update  
RUN apt-get -y -q install ntopng ntopng-data tzdata  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 3000  
CMD ["ntopng"]  

