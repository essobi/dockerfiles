FROM alpine:3.5  
MAINTAINER Stanislav Vitkovskiy <stas.vitkovsky@gmail.com>  
  
ENV SUBSONIC_VERSION=6.1.3 \  
SUBSONIC_USERID=1000 \  
SUBSONIC_PORT=4040 \  
SUBSONIC_HOME=/subsonic/home \  
SUBSONIC_MUSIC_FOLDER=/subsonic/music \  
SUBSONIC_PODCAST_FOLDER=/subsonic/podcasts \  
SUBSONIC_PLAYLIST_FOLDER=/subsonic/playlists  
  
# Install gosu  
COPY bin/gosu /bin/  
  
# Install required packages  
RUN apk add --no-cache openjdk8-jre-base ffmpeg openssl  
  
# Install Subsonic  
RUN install -d -D -o ${SUBSONIC_USERID} -m 0750 /subsonic
${SUBSONIC_HOME}/transcode ${SUBSONIC_MUSIC_FOLDER} ${SUBSONIC_PODCAST_FOLDER}
${SUBSONIC_PLAYLIST_FOLDER} && \  
wget -q -O - https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-${SUBSONIC_VERSION}-standalone.tar.gz | tar -C
/subsonic -xz && \  
ln -s /usr/bin/ffmpeg ${SUBSONIC_HOME}/transcode/  
  
VOLUME ["${SUBSONIC_HOME}", "${SUBSONIC_MUSIC_FOLDER}",
"${SUBSONIC_PODCAST_FOLDER}", "${SUBSONIC_PLAYLIST_FOLDER}"]  
  
COPY start.sh /subsonic/start.sh  
EXPOSE $SUBSONIC_PORT  
ENTRYPOINT ["/subsonic/start.sh"]  

