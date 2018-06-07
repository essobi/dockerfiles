FROM alpine:latest as downloader  
  
ENV SUBSONIC_VERSION 6.1.3  
RUN apk --no-cache add wget ca-certificates ffmpeg && \  
update-ca-certificates  
  
# Download subsonic-standalone  
RUN mkdir -p /opt/subsonic && \  
wget -O /opt/subsonic.tar.gz \  
https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-${SUBSONIC_VERSION}-standalone.tar.gz && \  
tar xfz /opt/subsonic.tar.gz -C /opt/subsonic && \  
rm -rf /opt/subsonic.tar.gz  
  
FROM java:8-jre-alpine  
  
MAINTAINER khiraiwa <the.world.nova@gmail.com>  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV SUBSONIC_HOME "/data_subsonic"  
ENV SUBSONIC_DEFAULT_MUSIC_FOLDER "/data_subsonic/music"  
ENV SUBSONIC_DEFAULT_PODCAST_FOLDER "/data_subsonic/music/Podcast"  
ENV SUBSONIC_DEFAULT_PLAYLIST_FOLDER "/data_subsonic/playlists"  
VOLUME ["/data_subsonic"]  
  
# Install ffmpeg, root certificates  
RUN apk --no-cache add ffmpeg ca-certificates && \  
update-ca-certificates  
  
RUN mkdir -p /data_subsonic/transcode && \  
ln -s /usr/bin/ffmpeg /data_subsonic/transcode/ffmpeg  
  
WORKDIR /root/  
EXPOSE 4040  
COPY \--from=downloader /opt/subsonic/subsonic-booter-jar-with-
dependencies.jar \  
/opt/subsonic/subsonic.war /opt/subsonic/subsonic.sh ./  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD ["help"]

