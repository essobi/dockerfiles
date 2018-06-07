FROM alpine:edge  
# copied in most parts from https://github.com/VITIMan/docker-music-
stack/blob/master/mpd  
MAINTAINER @gutmensch https://github.com/gutmensch  
  
ENV MPD_VERSION 0.20.18-r1  
ENV MPC_VERSION 0.29-r0  
  
# https://docs.docker.com/engine/reference/builder/#arg  
ARG user=mpd  
ARG group=audio  
  
RUN apk -q update \  
&& apk -q --no-progress add mpd="$MPD_VERSION" \  
&& apk -q --no-progress add mpc="$MPC_VERSION" \  
&& apk -q --no-progress add alsa-utils \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /var/lib/mpd/playlists \  
&& chown -R ${user}:${group} /var/lib/mpd  
  
VOLUME ["/var/lib/mpd", "/media/music"]  
  
COPY ./manifest/ /  
  
EXPOSE 6600  
EXPOSE 8800  
EXPOSE 8000  
CMD ["mpd", "--stdout", "--no-daemon"]  

