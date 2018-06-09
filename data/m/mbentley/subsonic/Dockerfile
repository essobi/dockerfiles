FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
# install ca-certificates, ffmpeg, and java8  
RUN (apk --no-cache add ca-certificates ffmpeg ttf-dejavu openjdk8 wget jq)  
  
# set libresonic major version  
ENV LIBRESONIC_MAJOR_VER="6"  
# create libresonic user  
RUN (mkdir /var/libresonic &&\  
addgroup -g 504 libresonic &&\  
adduser -h /var/libresonic -D -u 504 -g libresonic -G libresonic -s
/sbin/nologin libresonic &&\  
chown -R libresonic:libresonic /var/libresonic)  
  
# get latest libresonic version from GitHub, check to make sure it hasn't
passed the LIBRESONIC_MAJOR_VER and install libresonic.war from
https://github.com/Libresonic/libresonic  
RUN (LIBRESONIC_VER="$(wget -q -O -
https://api.github.com/repos/libresonic/libresonic/releases/latest | jq -r
.tag_name)" &&\  
if [ "$(echo $LIBRESONIC_VER | awk -F '.' '{print $1}')" !=
"v${LIBRESONIC_MAJOR_VER}" ]; then echo "Latest version number is no longer
${LIBRESONIC_MAJOR_VER}"; exit 1; fi &&\  
wget
"https://github.com/Libresonic/libresonic/releases/download/${LIBRESONIC_VER}/libresonic-${LIBRESONIC_VER}.war"
-O /var/libresonic/libresonic.war &&\  
chown libresonic:libresonic /var/libresonic/libresonic.war)  
  
# create transcode folder and add ffmpeg  
RUN (mkdir /var/libresonic/transcode &&\  
ln -s /usr/bin/ffmpeg /var/libresonic/transcode/ffmpeg &&\  
chown -R libresonic:libresonic /var/libresonic/transcode)  
  
# create data directories and symlinks to make it easier to use a volume  
RUN (mkdir /data &&\  
cd /data &&\  
mkdir db lucene2 lastfmcache thumbs music Podcast playlists .cache .java &&\  
touch libresonic.properties libresonic.log rollback.sql &&\  
cd /var/libresonic &&\  
ln -s /data/db &&\  
ln -s /data/lucene2 &&\  
ln -s /data/lastfmcache &&\  
ln -s /data/thumbs &&\  
ln -s /data/music &&\  
ln -s /data/Podcast &&\  
ln -s /data/playlists &&\  
ln -s /data/.cache &&\  
ln -s /data/.java &&\  
ln -s /data/libresonic.properties &&\  
ln -s /data/libresonic.log &&\  
ln -s /data/rollback.sql &&\  
chown -R libresonic:libresonic /data)  
  
COPY entrypoint.sh /entrypoint.sh  
  
USER libresonic  
WORKDIR /var/libresonic  
EXPOSE 4040  
VOLUME ["/data"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD
["java","-Dserver.address=0.0.0.0","-Dserver.port=4040","-Dserver.contextPath=/","-Djava.awt.headless=true","-jar","/var/libresonic/libresonic.war"]  

