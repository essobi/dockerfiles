FROM vsense/baseimage:alpine  
  
MAINTAINER Kevin Lefevre <klefevre@vsense.fr> (@archifleks)  
  
ENV BRANCH develop  
  
RUN apk --update add \  
git \  
tzdata \  
python \  
unrar \  
zip \  
libxslt \  
py-pip \  
py-lxml \  
&& apk --update add --virtual deps \  
python-dev \  
libxml2-dev \  
libxslt-dev \  
&& pip install \  
cheetah \  
&& git clone -b $BRANCH \--single-branch
https://github.com/SickRage/SickRage.git /sickrage \  
&& mkdir /config /downloads \  
&& adduser -D -h /sickrage -s /sbin/nologin -u 5001 sickrage \  
&& chown -R sickrage:sickrage /sickrage /config /downloads \  
&& apk del deps \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /config /downloads  
  
EXPOSE 8081  
USER sickrage  
  
CMD ["--datadir=/config", "--nolaunch"]  
  
ENTRYPOINT ["/usr/bin/env","python2","/sickrage/SickBeard.py"]  

