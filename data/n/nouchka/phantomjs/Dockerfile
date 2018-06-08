FROM debian:stable-slim  
LABEL maintainer="Jean-Avit Promis docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-phantomjs"  
LABEL version="latest"  
  
RUN apt-get update --fix-missing && \  
apt-get update && \  
apt-get install -y -q wget ca-certificates bzip2 libfontconfig unzip cron  
  
ARG PHANTOMJS_VERSION=2.1.1  
ARG
PHANTOMJS_FILE_SHA256SUM=86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f  
  
RUN cd /tmp && \  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2
-O phantomjs.tar.bz2 && \  
echo "${PHANTOMJS_FILE_SHA256SUM} /tmp/phantomjs.tar.bz2"| sha256sum -c - && \  
mkdir -p /tmp/phantomjs && \  
tar xf /tmp/phantomjs.tar.bz2 --strip-components=1 -C /tmp/phantomjs && \  
cp /tmp/phantomjs/bin/phantomjs /usr/local/bin/ && \  
chmod +x /usr/local/bin/phantomjs  
  
COPY loadspeed.js /usr/local/share/loadspeed.js  
RUN chmod 777 /usr/local/share/loadspeed.js  
  
RUN apt-get purge --auto-remove -y wget bzip2 unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer/workspace && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/developer  
  
WORKDIR /home/developer/workspace  
USER developer  
  
ADD start.sh /start.sh  
  
ENTRYPOINT [ "phantomjs" ]  
  
##ARG YSLOW_VERSION=3.1.8  
##ARG
YSLOW_FILE_SHA256SUM=661e1e48d3b39b7d3139926354e8248b46283649e280d8830cac6507b9666d61  
##RUN cd /tmp && \  
## wget http://yslow.org/yslow-phantomjs-${YSLOW_VERSION}.zip -O yslow.zip &&
\  
## echo "${YSLOW_FILE_SHA256SUM} /tmp/yslow.zip"| sha256sum -c - && \  
## unzip /tmp/yslow.zip && \  
## cp /tmp/yslow.js /usr/local/share/yslow.js  
##ARG
CONFIG_FILE_SHA256SUM=5ea0ed8613d7859ffcc6210822368d656331008575fb6444872e7babc41907ee  
##RUN cd /tmp && \  
## wget
https://raw.githubusercontent.com/jamesgpearce/confess/master/config.json -O
config.json && \  
## echo "${CONFIG_FILE_SHA256SUM} /tmp/config.json"| sha256sum -c - && \  
## cp /tmp/config.json /usr/local/share/  
##ARG
CONFIG_FILE_SHA256SUM=d1beec9e304b5d89fd5f6786444852d41ba89b9c02cee849939ef85820397946  
##RUN cd /tmp && \  
## wget
https://raw.githubusercontent.com/jamesgpearce/confess/master/confess.js -O
confess.js && \  
## echo "${CONFIG_FILE_SHA256SUM} /tmp/confess.js"| sha256sum -c - && \  
## cp /tmp/confess.js /usr/local/share/  

