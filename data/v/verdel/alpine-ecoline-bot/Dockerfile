FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
COPY rootfs /  
  
RUN apk --no-cache --update add \  
bash \  
py-pip \  
&& pip install --upgrade pip \  
&& pip install -r /opt/ecoline-telegram-bot/requirements.txt \  
# Clean up  
&& rm -rf \  
/tmp/* \  
/var/cache/apk/*  

