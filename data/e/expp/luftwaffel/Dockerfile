FROM python:3-alpine  
MAINTAINER Josh Elsasser <josh@elsasser.ca>  
  
# install the base CloudBot application + dependencies  
# (yes, there are a lot of them...)  
RUN apk add --no-cache \  
build-base \  
enchant-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
zlib-dev \  
&& pip install \  
https://github.com/jaelsasser/CloudBot/archive/setuptools.tar.gz \  
&& apk del --no-cache \  
build-base \  
enchant-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
zlib-dev \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /data /config  
  
VOLUME /data  
ADD ./plugins /plugins  
  
CMD [ \  
"cloudbot", "--config", "/data/config.json", \  
"--plugin-dir", "/plugins", \  
"--data", "/data", \  
"--logs", "/var/log/" \  
]  

