FROM xataz/mono  
MAINTAINER xataz <https://github.com/xataz>  
  
ENV GID=991 UID=991  
RUN echo "@testing http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add -U libmediainfo@testing \  
imagemagick \  
sqlite \  
ffmpeg \  
unzip \  
supervisor && \  
mkdir /embyServer && mkdir /embyData && cd /embyServer && \  
wget
https://github.com/MediaBrowser/Emby.Releases/raw/master/Server/Emby.Mono.zip
&& \  
unzip Emby.Mono.zip && \  
apk del unzip && rm -rf /var/cache/apk/* && rm -f Emby.Mono.zip  
  
EXPOSE 8096  
VOLUME /embyData  
ADD rootfs /  
RUN chmod +x /usr/bin/startup  
  
CMD ["tini","--","startup"]  

