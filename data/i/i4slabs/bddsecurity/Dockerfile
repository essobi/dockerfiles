FROM python:3.5-alpine  
  
#===================  
# environment  
#===================  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
ENV DISPLAY :0.0  
#===================  
# Jenkins user  
#===================  
ARG user=jenkins  
ARG group=jenkins  
ARG uid=1000  
ARG gid=1000  
ENV BEHAVE_HOME /opt/bdd  
RUN addgroup -g ${gid} ${group} && \  
adduser -u ${uid-} -D -G ${group} -s /bin/bash ${user} && \  
mkdir -p $BEHAVE_HOME && \  
chown $user:$group $BEHAVE_HOME  
  
#===================  
# Python requirement  
#===================  
ENV ZAP 2.6.0  
ADD requirements.txt /opt/bdd/requirements.txt  
  
#===================  
# Requisites  
#===================  
RUN \  
apk update && \  
apk add bash build-base xvfb libexif udev openssl \  
openssl-dev libffi-dev musl-dev \  
chromium chromium-chromedriver openjdk8-jre \  
nmap nmap-scripts nmap-ncat nmap-nping nmap-nselibs && \  
# install requiretments  
pip install -r /opt/bdd/requirements.txt && \  
pip install requests[security] && \  
# remove unused packages  
apk del openssl-dev libffi-dev musl-dev build-base && \  
rm -rf /var/cache/apk/* && \  
# zaproxy  
wget -P /tmp/
https://github.com/zaproxy/zaproxy/releases/download/${ZAP}/ZAP_${ZAP}_Linux.tar.gz
&& \  
tar -zxvf /tmp/ZAP_${ZAP}_Linux.tar.gz && \  
mv -f ZAP_${ZAP} /opt/zap && \  
rm -rf /tmp/ZAP_${ZAP}_Linux.tar.gz  
  
  
WORKDIR /opt/bdd  
USER jenkins  

