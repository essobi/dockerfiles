FROM ubuntu  
MAINTAINER Rusty Bower  
  
# install packages  
RUN apt-get update  
RUN apt-get install -y cpanminus cron gcc make wget  
  
# install Data::Dumper  
RUN cpanm Data::Dumper  
  
# download and install pisg  
RUN wget -O /tmp/pisg-0.73.tar.gz
http://prdownloads.sourceforge.net/pisg/pisg-0.73.tar.gz  
RUN tar zxvf /tmp/pisg-0.73.tar.gz -C /opt  
  
# copy crontab into place  
# start cron  
RUN service cron start  
  
# cleanup  
RUN apt-get clean  
RUN rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
# add local files  
# COPY root/ /  
# ports and volumes  
VOLUME /nginx /logs /cache /config  
  
ENTRYPOINT /opt/pisg-0.73/pisg -co /config/pisg.cfg -o /nginx/index.html

