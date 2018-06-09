FROM tiredofit/nginx-php-fpm:7.1-latest  
LABEL maintainer="Dave Conroy (dave at tiredofit dot ca)"  
### Set Environment Variables  
ENV TEAMPASS_VERSION=2.1.27.16  
### Dependencies Installation  
  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing \  
gnu-libiconv \  
&& \  
  
rm -rf /var/cache/apk/*  
  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
### Files Addition  
ADD install /  
  

