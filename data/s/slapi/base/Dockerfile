FROM alpine:3.6  
  
MAINTAINER SLAPI Devs  
  
RUN apk update  
RUN apk add \  
bash \  
gnupg \  
tar \  
git \  
zip \  
curl \  
wget \  
openssl \  
ca-certificates \  
libffi \  
gdbm \  
ncurses \  
readline \  
tzdata \  
openssl-dev \  
zlib-dev \  
libxml2-dev \  
libxslt-dev \  
build-base \  
libgcrypt &&\  
rm /var/cache/apk/* &&\  
mkdir -p /scripts  
  
VOLUME /scripts  
  
WORKDIR /scripts  

