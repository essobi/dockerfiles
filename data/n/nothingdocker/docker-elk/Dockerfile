# Version 1.0.1  
FROM sebp/elk  
RUN cd /usr/local;\  
curl -L -O
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.2.2-amd64.deb;\  
dpkg -i filebeat-5.2.2-amd64.deb;\  
rm -f filebeat-5.2.2-amd64.deb;  
  
RUN apt-get update  
RUN apt-get install tzdata  
RUN apt-get install net-tools  
  
COPY ./tool /data  
RUN echo '0 0 * * * /data/tool/auto_clear.sh' >> /etc/cron.d/elk.cron \  
&& crontab /etc/cron.d/elk.cron  
  
RUN rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
USER logstash  
RUN mkdir -p /etc/logstash  
  
VOLUME /etc/logstash  
#RUN chown -R logstash:logstash /etc/logstash  
USER root  

