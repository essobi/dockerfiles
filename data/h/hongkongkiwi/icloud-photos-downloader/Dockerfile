FROM alpine:latest  
  
RUN set -xe && \  
apk add --update --no-cache python py-pip git && \  
git clone https://github.com/ndbroadbent/icloud_photos_downloader.git && \  
pip2 install -r icloud_photos_downloader/requirements.txt && \  
adduser -D -h /home/docker -u 1001 docker && \  
rm -fr /var/cache/apk/*  
  
USER docker  
  
WORKDIR /icloud_photos_downloader  

