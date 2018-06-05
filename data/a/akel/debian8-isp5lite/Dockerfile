FROM debian:jessie  
MAINTAINER Akel <akel@maintainer.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install wget  
RUN apt-get -y install bsdmainutils  
RUN apt-get -y install openssh-server  
  
RUN echo "deb http://download.ispsystem.com/repo/debian base-jessie main" >
/etc/apt/sources.list.d/ispsystem-base.list  
RUN echo "deb http://download.ispsystem.com/repo/debian stable-jessie main" >
/etc/apt/sources.list.d/ispsystem.list  
  
RUN apt-get -y update  
RUN apt-get --reinstall install bsdutils  
RUN apt-get -y --force-yes install ispmanager-lite-common  
  
COPY postinstall.sh /usr/local/src/postinstall.sh  
COPY tuning.sh /usr/local/src/tuning.sh  
COPY genkeys.sh /usr/local/src/genkeys.sh  
  
RUN chmod +x /usr/local/src/postinstall.sh  
RUN chmod +x /usr/local/src/tuning.sh  
RUN chmod +x /usr/local/src/genkeys.sh  
  
RUN /usr/local/src/postinstall.sh  
RUN /usr/local/src/tuning.sh  
  
EXPOSE 21 22 25 53 80 110 143 443 465 1500 3306  

