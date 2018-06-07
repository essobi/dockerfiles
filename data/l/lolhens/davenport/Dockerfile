FROM lolhens/baseimage-openjre:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
ENV DAVENPORT_VERSION 0.9.11  
ENV DAVENPORT_NAME davenport-$DAVENPORT_VERSION  
ENV DAVENPORT_FILE $DAVENPORT_NAME.zip  
ENV DAVENPORT_URL
http://downloads.sourceforge.net/project/davenport/davenport/$DAVENPORT_VERSION/$DAVENPORT_FILE  
  
  
RUN cd "/tmp" \  
&& curl -LO $DAVENPORT_URL \  
&& unzip $DAVENPORT_FILE \  
&& mv $DAVENPORT_NAME "/opt/davenport/" \  
&& cleanimage  
  
RUN appfolders add "davenport/web.xml" "/opt/davenport/webapps/root/WEB-
INF/web.xml"  
  
WORKDIR /opt/davenport/  
CMD java -jar start.jar  
  
VOLUME /usr/local/appdata/davenport  
  
EXPOSE 8080  

