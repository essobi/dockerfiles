FROM ubuntu:trusty  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FDA5DFFC && \  
echo 'deb http://apt.sonarr.tv/ master main' >
/etc/apt/sources.list.d/nzbdrone.list && \  
apt-get update -q  
  
RUN apt-get install -qy libmono-cil-dev nzbdrone  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* var/tmp/*  
  
ADD start.sh /start.sh  
ADD update.sh /update.sh  
  
VOLUME ["/config"]  
VOLUME ["/library"]  
VOLUME ["/downloads"]  
EXPOSE 8989  
CMD ["/bin/bash", "/start.sh"]  

