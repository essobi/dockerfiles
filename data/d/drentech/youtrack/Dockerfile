FROM drentech/java:stable  
  
MAINTAINER Marian Sievers <info@mariansievers.de>  
  
# pre-requirements  
RUN mkdir -p /opt/youtrack && mkdir -p /srv/database && mkdir -p /srv/backup  
  
# install YouTrack  
RUN wget http://download.jetbrains.com/charisma/youtrack-6.5.16807.zip && mv
youtrack-6.5.16807.zip /opt/youtrack/  
RUN cd /opt/youtrack && unzip youtrack-6.5.16807.zip  
  
# clean up  
RUN rm /opt/youtrack/youtrack-6.5.16807.zip  
  
VOLUME /srv/database  
VOLUME /srv/backup  
  
EXPOSE 8080  
WORKDIR /opt/youtrack  
ENTRYPOINT /opt/youtrack/bin/youtrack.sh run  

