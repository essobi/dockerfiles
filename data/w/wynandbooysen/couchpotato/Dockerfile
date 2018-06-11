FROM alpine:latest  
MAINTAINER Wynand Booysen  
  
#Installation  
RUN apk -U upgrade && \  
apk -U add \  
ca-certificates git \  
py2-pip ca-certificates git python py-libxml2 py-lxml py-pip \  
make gcc g++ python-dev openssl-dev libffi-dev \  
&& \  
pip --no-cache-dir install pyopenssl && \  
git clone \--depth 1 https://github.com/RuudBurger/CouchPotatoServer.git
/CouchPotatoServer && \  
apk del make gcc g++ python-dev && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
#Volumes  
VOLUME ["/config", "/downloads", "/movies"]  
  
#Ports  
EXPOSE 5050  
#Start-up script  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
CMD ["/start.sh"]  

