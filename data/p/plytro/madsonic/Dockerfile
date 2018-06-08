FROM ubuntu:14.10  
RUN locale-gen en_US en_US.UTF-8  
  
RUN apt-get update  
RUN apt-get -qqy --force-yes dist-upgrade  
RUN apt-get install -qqy --force-yes wget default-jre-headless  
  
RUN wget http://madsonic.org/download/5.1/20141017_madsonic-5.1.5200.deb  
RUN dpkg -i 20141017_madsonic-5.1.5200.deb  
  
VOLUME /config  
VOLUME /data  
  
EXPOSE 4040  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
  

