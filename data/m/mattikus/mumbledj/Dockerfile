FROM alpine:latest  
MAINTAINER Matt Kemp <matt@mattikus.com>  
  
COPY docker-entrypoint.sh /  
RUN chmod a+x /docker-entrypoint.sh  
RUN apk add \--update \  
aria2 \  
ca-certificates \  
ffmpeg \  
gcc \  
git \  
go \  
musl-dev \  
openal-soft-dev \  
openssl \  
opus-dev \  
python \  
&& wget https://yt-dl.org/downloads/latest/youtube-dl -O /bin/youtube-dl &&
chmod a+x /bin/youtube-dl \  
&& GOPATH=/ go get -u -v github.com/matthieugrieger/mumbledj \  
&& mkdir -p /root/.config \  
&& apk del gcc go git musl-dev && rm -rf /var/cache/apk/* /pkg /src  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["--config", "/etc/mumbledj.yaml"]  

