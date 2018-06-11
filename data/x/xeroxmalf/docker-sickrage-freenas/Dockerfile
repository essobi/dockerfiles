FROM alpine:3.5  
  
LABEL org.freenas.interactive="false" \  
org.freenas.version="3" \  
org.freenas.upgradeable="true" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.web-ui-protocol="http" \  
org.freenas.web-ui-port="8081" \  
org.freenas.web-ui-path="" \  
org.freenas.port-mappings="8081:8081/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/config\", \  
\"descr\": \"Sickrage config files\" \  
}, \  
{ \  
\"name\": \"/downloads\", \  
\"descr\": \"Sickrage downloads volume\" \  
}, \  
{ \  
\"name\": \"/tv\", \  
\"descr\": \"Location of TV library\" \  
} \  
]"  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm'  
  
RUN apk -U add --no-cache \  
py2-pip ca-certificates git python py-libxml2 py-lxml \  
make gcc g++ python-dev openssl-dev libffi-dev unrar tzdata \  
&& \  
pip --no-cache-dir install --upgrade setuptools && \  
pip --no-cache-dir install --upgrade pyopenssl cheetah requirements && \  
git clone --depth 1 https://github.com/SickRage/SickRage.git /sickrage && \  
apk del make gcc g++ python-dev && \  
rm -rf /tmp && \  
rm -rf /var/cache/apk/*  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
CMD ["/start.sh"]  

