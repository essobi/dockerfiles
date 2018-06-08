FROM nginx:1.13.3-alpine  
MAINTAINER Chris Garrett (https://github.com/chris-garrett/docker-nginx)  
LABEL description="Nginx image 1.13.3"  
  
ARG DOCKERIZE_VERSION=v0.5.0  
COPY ./bash_aliases /home/nginx/.bashrc  
COPY ./vimrc /home/nginx/.vimrc  
  
RUN apk --no-cache add -U \  
ca-certificates \  
openssl \  
&& update-ca-certificates \  
  
&& apk --no-cache add -U \  
bash \  
vim \  
wget \  
curl \  
  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
  
&& chown nginx:nginx /home/nginx/.bashrc /home/nginx/.vimrc \  
&& ln -sf /usr/bin/vim /usr/bin/vi  
  
#USER nginx  

