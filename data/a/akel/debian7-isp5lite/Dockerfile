# VERSION 0.0.1  
FROM debian:wheezy  
MAINTAINER Akel <akel@maintainer.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y install wget  
RUN apt-get -y install bsdmainutils  
RUN apt-get -y install openssh-server  
  
RUN apt-get install -y supervisor bindfs  
RUN service supervisor stop  
  
RUN echo "deb http://cdn.ispsystem.com/repo/debian base-wheezy main" >
/etc/apt/sources.list.d/ispsystem-base.list  
RUN echo "deb http://cdn.ispsystem.com/repo/debian stable-wheezy main" >
/etc/apt/sources.list.d/ispsystem.list  
  
RUN apt-get -y update  
RUN apt-get \--reinstall install bsdutils  
RUN apt-get -y --force-yes install ispmanager-lite-common  
  
COPY postinstall.sh /usr/local/src/postinstall.sh  
COPY tuning.sh /usr/local/src/tuning.sh  
  
RUN chmod +x /usr/local/src/postinstall.sh  
RUN chmod +x /usr/local/src/tuning.sh  
  
RUN /usr/local/src/postinstall.sh  
RUN /usr/local/src/tuning.sh  
  
EXPOSE 21 22 25 53 80 110 143 443 465 1500 3306  

