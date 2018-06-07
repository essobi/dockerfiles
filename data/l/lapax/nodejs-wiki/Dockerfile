FROM ubuntu:trusty  
#FROM lapax/trusty-dev  
MAINTAINER Lex Lapax <lexlapax@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu trusty main universe" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y wget curl build-essential libwrap0-dev libssl-dev
python-distutils-extra libleveldb-dev libleveldb1 nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g wiki  
RUN apt-get clean -y  
EXPOSE 3000  
CMD ["/usr/local/bin/wiki", "-p", "3000"]  
  

