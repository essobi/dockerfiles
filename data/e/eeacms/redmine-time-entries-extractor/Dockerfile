FROM alpine  
  
RUN apk add --update git unzip openntpd openjdk8-jre bash nodejs curl git
nodejs-npm  
  
RUN npm install elasticdump -g  
RUN git clone -b 0.0.2 https://github.com/eea/redmine-time-entries-
extractor.git  
  
RUN unzip redmine-time-entries-
extractor/redmine_time_entries_extractor_0.1.zip -d /opt  
RUN chmod a+x
/opt/redmine_time_entries_extractor/redmine_time_entries_extractor_run.sh  
  
COPY ingestData.sh /opt  
COPY ingestConfiguration.sh /opt  
RUN chmod a+x /opt/*.sh  
  
RUN mkdir -p /var/spool/cron/crontabs  
COPY time_entries.conf /  
  
WORKDIR /opt  
  
COPY docker-entrypoint.sh /  
RUN chmod a+x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ntpd -p pool.ntp.org && echo "$CRON_ENTRY" /opt/ingestData.sh | crontab -
&& crond -f  

