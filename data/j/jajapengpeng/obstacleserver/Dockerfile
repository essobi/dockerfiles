FROM alpine:3.5  
MAINTAINER Vincent Parizet <vincent.parizet@hotmail.fr>  
  
ENV DEDICATED_URL
http://files.v04.maniaplanet.com/server/ManiaplanetServer_Latest.zip  
ENV PROJECT_DIR /dedicated  
  
WORKDIR /dedicated  
  
# Install several dependencies.  
RUN apk update \  
&& apk add --no-cache unzip wget ca-certificates  
  
# Link the musl to glibc as it's compatible (required in Alpine image).  
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget -q https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk \  
&& apk add glibc-2.25-r0.apk  
  
# Download latest dedicated files  
RUN wget $DEDICATED_URL -qO /tmp/dedicated.zip  
  
# Create folder and unpack, cleanup, prepare executables etc.  
RUN mkdir -p $PROJECT_DIR \  
&& unzip -quo /tmp/dedicated.zip -d $PROJECT_DIR \  
&& rm /tmp/dedicated.zip \  
&& rm -rf $PROJECT_DIR/*.bat $PROJECT_DIR/*.exe $PROJECT_DIR/*.html
$PROJECT_DIR/RemoteControlExamples \  
&& chmod +x $PROJECT_DIR/ManiaPlanetServer \  
&& mkdir -p $PROJECT_DIR/GameData \  
&& mkdir -p $PROJECT_DIR/UserData \  
&& mkdir -p $PROJECT_DIR/UserData/Config \  
&& mkdir -p $PROJECT_DIR/UserData/Packs \  
&& mkdir -p $PROJECT_DIR/UserData/Maps/MatchSettings  
  
RUN wget
https://v4.live.maniaplanet.com/ingame/public/titles/download/obstacle@smokegun.Title.Pack.gbx
-qO $PROJECT_DIR/Packs/obstacle@smokegun.Title.Pack.gbx  
  
# Install the dedicated configuration file(s).  
ADD files/config.default.xml $PROJECT_DIR/config.txt  
ADD files/matchsettings.default.xml $PROJECT_DIR/matchsettings.txt  
ADD files/test.Map.Gbx $PROJECT_DIR/test.Map.Gbx  
  
# Install run script.  
ADD entrypoint.sh $PROJECT_DIR/start.sh  
RUN chmod +x $PROJECT_DIR/start.sh  
  
EXPOSE 2350 2350/udp 3450 3450/udp 5000  
CMD [ "./start.sh" ]  

