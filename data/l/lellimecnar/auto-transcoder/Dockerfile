FROM node:alpine  
MAINTAINER lellimecnar  
  
ENV SCHEDULE="* * * * *" \  
SCHEDULE_QUEUE="*/30 * * * *" \  
MEDIA_WATCH_DIR="/watch" \  
ALLOWED_VIDEO_CODECS="libx264,h264,h.264" \  
ALLOWED_AUDIO_CODECS="aac,libfaac,ac3,libmp3lame,mp3,mp2" \  
ALLOWED_EXTENSIONS="mp4,mkv"  
RUN apk add --no-cache \  
ffmpeg  
  
COPY root/ /  
  
RUN chmod +x /usr/local/bin/*  
RUN chmod 0644 /etc/crontabs/*  
  
WORKDIR /opt/auto-transcoder  
RUN yarn  
  
VOLUME /watch  
  
CMD ["/usr/local/bin/init"]  

