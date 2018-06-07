FROM debian:stable-slim  
MAINTAINER WebNL <info@webnl.nl>  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod 777 /usr/local/bin/run.sh  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# setup workdir  
WORKDIR /root/work/  
  
# install git  
RUN apt-get -y update && apt-get -y install git  
  
# install git-ftp  
RUN apt-get -y install git-ftp  
  
# install ftp  
RUN apt-get -y install ncftp  
  
# install wget  
RUN apt-get -y install wget  
  
# slim down image  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/man/?? /usr/share/man/??_*  
  
# CMD /usr/local/bin/run.sh

