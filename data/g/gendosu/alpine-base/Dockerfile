# alpine-base  
#  
# VERSION 0.0.1  
  
FROM alpine:latest  
  
MAINTAINER Gen Takahashi <gendosu@gmail.com>  
  
RUN apk add --update \  
bash \  
git \  
wget \  
curl \  
vim \  
build-base \  
readline-dev \  
openssl-dev \  
zlib-dev \  
&& rm -rf /var/cache/apk/*  
  
# # Timezone変更  
RUN apk add --update \  
tzdata \  
&& cp /usr/share/zoneinfo/Japan /etc/localtime \  
&& apk del tzdata \  
&& rm -rf /var/cache/apk/*  
  

