FROM alpine:latest  
MAINTAINER Wynand Booysen  
  
RUN apk -U upgrade && \  
apk -U add \  
ca-certificates \  
py2-pip ca-certificates git python py-libxml2 py-lxml \  
make gcc g++ python-dev openssl-dev libffi-dev unrar \  
&& \  
pip --no-cache-dir install pyopenssl cheetah requirements && \  
git clone \--depth 1 https://github.com/SickRage/SickRage.git /sickrage && \  
apk del make gcc g++ python-dev && \  
rm -rf /tmp && \  
rm -rf /var/cache/apk/*  
  
#Volumes  
VOLUME ["/config", "/downloads", "/data", "/cache"]  
  
#Ports  
EXPOSE 8081  
#Start-up script  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
CMD ["/start.sh"]  

