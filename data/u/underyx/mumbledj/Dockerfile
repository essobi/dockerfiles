FROM alpine:3.4  
MAINTAINER Bence Nagy <bence@underyx.me>  
  
RUN apk add \--no-cache --virtual=.build-deps gcc git go musl-dev &&\  
apk add \--no-cache --virtual=.run-deps aria2 ca-certificates ffmpeg openal-
soft-dev openssl opus-dev python &&\  
wget https://yt-dl.org/downloads/latest/youtube-dl -O /bin/youtube-dl &&\  
chmod a+x /bin/youtube-dl &&\  
GOPATH=/ go get -u -v github.com/matthieugrieger/mumbledj &&\  
mkdir -p /root/.config &&\  
apk del .build-deps &&\  
rm -rf /pkg /src  
  
ENTRYPOINT ["/bin/mumbledj"]  
CMD ["--config", "/etc/mumbledj.yaml"]  

