FROM lsiobase/alpine.nginx:3.6  
MAINTAINER chbmb  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
WORKDIR /usr/share/webapps  
# install packages  
RUN \  
apk add --no-cache \  
curl \  
imagemagick \  
mc \  
php7-curl \  
php7-exif \  
php7-gd \  
php7-imagick \  
php7-mbstring \  
php7-mysqli \  
php7-mysqlnd \  
php7-zip \  
re2c \  
git && \  
mkdir -p /usr/share/webapps/ && \  
git clone -b feature/subalbums https://github.com/etheld/Lychee.git lychee &&
\  
rm -rf /tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
EXPOSE 80  
VOLUME /config /pictures  

