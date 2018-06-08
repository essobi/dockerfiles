##  
## SmartHomeNG.py  
##  
## Use latest python 3.5 Alpine based images as starting point  
FROM python:3.5-alpine  
  
## Choose between master or develop branch (or any other)  
ARG BRANCH=develop  
  
## Images labels  
LABEL version = "1.0" \  
description = "SmartHomeNG image"  
maintainer = "Serge Wagener serge@wagener.family"  
## Install SmartHomeNG and needed dependencies  
RUN apk add --no-cache git build-base linux-headers \  
&& adduser smarthome -D -g "SmartHomeNG User" \  
&& cd /usr/local \  
&& git clone git://github.com/smarthomeNG/smarthome.git --branch $BRANCH \  
&& cd ./smarthome \  
&& ./bin/fetch_plugins.sh \  
&& chown -R smarthome:smarthome /usr/local/smarthome \  
&& mkdir -p /usr/local/smarthome/var/run/ && mkdir -p /usr/local/examples/etc
\  
&& cd /usr/local/smarthome/ && pip install -r requirements/all.txt && pip
install pymysql telepot \  
&& apk del build-base linux-headers  
  
COPY check_for_mysql.py /  
COPY entrypoint.sh /  
COPY *.yaml /usr/local/smarthome/etc/  
COPY *.yaml /usr/local/examples/etc/  
  
## WebSocket, Backend  
EXPOSE 2424 8383  
## User modifiable files  
VOLUME /var/www/html /usr/local/smarthome/etc /usr/local/smarthome/items
/usr/local/smarthome/logics /usr/local/smarthome/scenes  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["-d"]  

