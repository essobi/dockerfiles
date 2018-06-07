FROM lolhens/baseimage:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
ENV TELEPORT_VERSION 2.0.2  
ENV TELEPORT_NAME teleport  
ENV TELEPORT_FILE $TELEPORT_NAME-v$TELEPORT_VERSION-linux-amd64-bin.tar.gz  
ENV TELEPORT_URL
https://github.com/gravitational/teleport/releases/download/v$TELEPORT_VERSION/$TELEPORT_FILE  
ENV TELEPORT_HOME /usr/local/teleport  
  
ENV TELEPORT_NODENAME node  
  
  
RUN apt-get update \  
&& apt-get install -y \  
make \  
&& cd "/tmp" \  
&& curl -LO $TELEPORT_URL \  
&& tar -xf $TELEPORT_FILE \  
&& mv $TELEPORT_NAME $TELEPORT_HOME \  
&& cd $TELEPORT_HOME \  
&& make install \  
&& cleanimage  
  
RUN appfolders add "teleport" "/var/lib/teleport"  
  
WORKDIR $TELEPORT_HOME  
CMD teleport start --nodename=$TELEPORT_NODENAME  
  
VOLUME /usr/local/appdata/teleport  
  
EXPOSE 3022 3023 3024 3025 3080  

