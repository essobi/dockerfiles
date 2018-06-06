FROM java:7  
MAINTAINER Go About <tech@goabout.com>  
  
ENV VERSION=master \  
PLAY_VERSION=1.2.5  
ADD https://github.com/conveyal/gtfs-editor/archive/$VERSION.zip /tmp/gtfs-
editor-$VERSION.zip  
ADD https://downloads.typesafe.com/releases/play-$PLAY_VERSION.zip
/tmp/play-$PLAY_VERSION.zip  
  
RUN cd /opt && \  
unzip /tmp/gtfs-editor-$VERSION.zip && \  
ln -s gtfs-editor-$VERSION gtfs-editor && \  
rm /tmp/gtfs-editor-$VERSION.zip && \  
unzip /tmp/play-$PLAY_VERSION.zip && \  
ln -s play-$PLAY_VERSION play && \  
rm /tmp/play-$PLAY_VERSION.zip  
  
WORKDIR /opt/gtfs-editor  
  
RUN ../play/play dependencies && \  
mkdir /opt/gtfs-editor/public/data  
  
VOLUME /opt/gtfs-editor/data  
  
EXPOSE 9000  
CMD ["../play/play", "run"]  

