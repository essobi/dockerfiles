FROM python:3-alpine  
MAINTAINER Michal Kubenka <mkubenka@gmail.com>  
  
# https://github.com/madnight/docker-alpine-wkhtmltopdf  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --update --no-cache \  
libgcc \  
libstdc++ \  
libx11 \  
glib \  
libxrender \  
libxext \  
libintl \  
fonts-base \  
&& rm -rf /var/cache/apk/*  
  
ADD wkhtmltopdf /usr/bin/  
  
CMD [ "python3" ]  

