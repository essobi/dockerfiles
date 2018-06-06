FROM alpine:edge  
MAINTAINER Tim Haak <tim@haak.co>  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm'  
RUN apk -U upgrade && \  
apk -U add \  
ca-certificates \  
git \  
openssl \  
python \  
py2-pip py2-openssl py-libxml2 py2-lxml \  
&& \  
apk --update add --virtual build-dependencies libffi-dev openssl-dev python-
dev py-pip build-base && \  
pip install --upgrade pip && \  
pip install --upgrade pyopenssl && \  
git clone \--depth 1 https://github.com/CouchPotato/CouchPotatoServer.git
/CouchPotatoServer && \  
apk del build-dependencies && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/config", "/data"]  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
EXPOSE 5050  
CMD ["/start.sh"]  

