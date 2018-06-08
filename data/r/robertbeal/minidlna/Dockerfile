FROM alpine:3.7  
MAINTAINER Robert Beal <rob@kohi.uk>  
  
RUN apk --no-cache add \  
curl \  
inotify-tools \  
ffmpeg \  
flac \  
libvorbis \  
libexif \  
libjpeg \  
libid3tag \  
minidlna \  
su-exec \  
&& rm -rf /tmp/*  
  
VOLUME /config /data  
EXPOSE 8200 1900/udp  
  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["-f", "/config/minidlna.conf", "-S"]  

