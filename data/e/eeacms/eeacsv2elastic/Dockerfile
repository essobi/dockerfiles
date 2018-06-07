FROM alpine  
  
RUN apk add --update git unzip openntpd openjdk8-jre bash nodejs curl git
nodejs-npm  
  
WORKDIR /opt  
  
ADD elasticsearch-csv /elasticsearch-csv  
RUN cd /elasticsearch-csv && npm install -g  
  
#RUN npm install elasticsearch-csv  
RUN npm install elasticdump -g  
  
RUN mkdir -p /var/spool/cron/crontabs  
  
COPY ingestData.js /opt/ingestData.js  
COPY ingestConfiguration.sh /opt/ingestConfiguration.sh  
COPY ingestData.sh /opt/ingestData.sh  
COPY docker-entrypoint.sh /  
  
RUN chmod a+x /opt/ingestData.sh /opt/ingestConfiguration.sh /docker-
entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ntpd -p pool.ntp.org && echo "$CRON_ENTRY" /opt/ingestData.sh | crontab -
&& crond -f  

