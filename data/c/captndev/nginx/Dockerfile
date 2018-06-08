FROM alpine:latest  
MAINTAINER Philip Graf <philip.graf@novapo.net>  
  
ADD etc /etc  
  
RUN apk update && \  
apk upgrade && \  
apk add \  
ca-certificates \  
curl \  
bash \  
bash-completion \  
ncurses \  
vim \  
gettext \  
logrotate \  
tar \  
rsync \  
shadow@testing && \  
rm -rf /var/cache/apk/*  
  
RUN groupadd \  
-g 1000 \  
nginx && \  
useradd \  
-u 1000 \  
-g nginx \  
-s /bin/sh \  
-m \  
nginx && \  
apk update && \  
apk add \  
nginx && \  
rm -rf /var/cache/apk/*  
  
RUN curl -sLo /usr/local/bin/ep
https://github.com/kreuzwerker/envplate/releases/download/v0.0.8/ep-linux &&
chmod +x /usr/local/bin/ep  
  
ADD docker-entrypoint.sh /entrypoint.sh  
  
CMD [ "/entrypoint.sh" ]  

