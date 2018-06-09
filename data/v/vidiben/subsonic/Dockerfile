FROM alpine:3.6  
MAINTAINER Benoît Vidis <contact@benoitvidis.com>  
  
ENV SUBSONIC_VERSION=6.1.3  
ENV SUBSONIC_ROOT=/opt/subsonic  
ENV SUBSONIC_DEFAULT_MUSIC_FOLDER=/var/subsonic/music  
ENV SUBSONIC_DEFAULT_PODCAST_FOLDER=/var/subsonic/podcast  
ENV SUBSONIC_DEFAULT_PLAYLIST_FOLDER=/var/subsonic/playlists  
  
LABEL version="$SUBSONIC_VERSION"  
LABEL description="Subsonic media streamer v$SUBSONIC_VERSION"  
  
WORKDIR "${SUBSONIC_ROOT}"  
  
RUN set -x \  
&& apk add --no-cache \  
curl \  
ffmpeg \  
lame \  
openjdk8-jre \  
\  
&& mkdir -p \  
"${SUBSONIC_ROOT}" \  
"${SUBSONIC_DEFAULT_MUSIC_FOLDER}" \  
"${SUBSONIC_DEFAULT_PODCAST_FOLDER}" \  
"${SUBSONIC_DEFAULT_PLAYLIST_FOLDER}" \  
&& curl -o subsonic.tar.gz -SLO "https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-${SUBSONIC_VERSION}-standalone.tar.gz" \  
&& tar -C "${SUBSONIC_ROOT}" -xvf "subsonic.tar.gz" \  
&& rm subsonic.tar.gz \  
\  
&& apk del \  
curl \  
\  
&& echo done  
  
COPY docker-entrypoint.sh /  
  
CMD ["/docker-entrypoint.sh"]  
  

