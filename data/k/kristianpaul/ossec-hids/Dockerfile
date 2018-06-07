FROM tutum/ubuntu  
  
MAINTAINER Cristian Paul <paul@kristianpaul.org>  
  
RUN apt-get -y install build-essential zip wget  
  
RUN wget https://github.com/kristianpaul/ossec-hids/archive/preloaded-
server.zip  
  
RUN unzip preloaded-server.zip  
  
RUN cd ossec-hids-preloaded-server/ && bash ./install.sh  
  
RUN apt-get purge -y --auto-remove build-essential zip wget  
  
VOLUME /srv/ossec/var/  
  
CMD ["/etc/init.d/ossec start"]  
  
EXPOSE 1514  
EXPOSE 514  

