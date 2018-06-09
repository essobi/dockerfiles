FROM alpine:3.3  
MAINTAINER Gergan Penkov <gergan at gmail.com>  
  
# install ca-certificates, ffmpeg, and java7  
RUN (echo "http://nl.alpinelinux.org/alpine//v3.3/main" >
/etc/apk/repositories &&\  
echo "http://nl.alpinelinux.org/alpine//v3.3/community" >>
/etc/apk/repositories &&\  
apk update &&\  
apk upgrade &&\  
apk --no-cache add libva ca-certificates ffmpeg flac lame openjdk7-jre-base
wget ttf-dejavu fontconfig &&\  
wget
"http://sourceforge.net/projects/subsonic/files/subsonic/5.3/subsonic-5.3-standalone.tar.gz/download"
-O /tmp/subsonic.tar.gz &&\  
mkdir /var/subsonic &&\  
tar zxf /tmp/subsonic.tar.gz -C /var/subsonic &&\  
rm /tmp/subsonic.tar.gz &&\  
wget
"https://github.com/EugeneKay/subsonic/releases/download/v5.3-kang/subsonic-v5.3-kang.war"
-O /var/subsonic/subsonic.war &&\  
apk del wget &&\  
addgroup -g 990 -S subsonic &&\  
adduser -G subsonic -S -u 990 -h /var/subsonic -D subsonic &&\  
mkdir /var/subsonic/transcode &&\  
ln -s $(which ffmpeg) /var/subsonic/transcode/ffmpeg && \  
ln -s $(which flac) /var/subsonic/transcode/flac && \  
ln -s $(which lame) /var/subsonic/transcode/lame && \  
chown -R subsonic:subsonic /var/subsonic/transcode &&\  
mkdir /data &&\  
cd /data &&\  
mkdir db jetty lucene2 lastfmcache thumbs music podcast playlists &&\  
touch subsonic.properties subsonic.log &&\  
cd /var/subsonic &&\  
ln -s /data/db &&\  
ln -s /data/jetty &&\  
ln -s /data/lucene2 &&\  
ln -s /data/lastfmcache &&\  
ln -s /data/thumbs &&\  
ln -s /music &&\  
ln -s /data/podcast &&\  
ln -s /data/playlists &&\  
ln -s /data/subsonic.properties &&\  
ln -s /data/subsonic.log &&\  
chown -R subsonic:subsonic /data)  
  
USER subsonic  
WORKDIR /var/subsonic  
EXPOSE 4040 4443  
VOLUME ["/data", "/music"]  
  
CMD
["java","-Xmx1024m","-Dsubsonic.home=/var/subsonic","-Dsubsonic.host=0.0.0.0","-Dsubsonic.port=4040","-Dsubsonic.httpsPort=4443","-Dsubsonic.contextPath=/","-Dsubsonic.defaultMusicFolder=/music","-Dsubsonic.defaultPodcastFolder=/data/podcast","-Dsubsonic.defaultPlaylistFolder=/data/playlists","-Djava.awt.headless=true","-jar","subsonic-
booter-jar-with-dependencies.jar"]  

