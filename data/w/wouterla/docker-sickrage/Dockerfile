FROM alpine:edge  
MAINTAINER Tim Haak <tim@haak.co.uk>  
  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm'  
RUN apk -U upgrade && \  
apk -U add \  
ca-certificates \  
py-pip ca-certificates git python py-libxml2 py-lxml \  
make gcc g++ python-dev openssl-dev libffi-dev unrar \  
&& \  
pip --no-cache-dir install pyopenssl cheetah requirements && \  
git clone \--depth 1 https://github.com/SickRage/SickRage.git /sickrage && \  
apk del make gcc g++ python-dev && \  
rm -rf /tmp && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/config", "/data", "/cache", "/scripts"]  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
EXPOSE 8081  
CMD ["/start.sh"]  

