FROM alpine:3.7  
MAINTAINER Loïck MAHIEUX <loick111@gmail.com>  
  
WORKDIR /app  
  
ENV OWNER "test"  
ENV INFLUXDB_URL "http://influxdb:8086"  
ENV INFLUXDB_DATABASE "telegraf"  
ENV INFLUXDB_RETENTION_POLICY ""  
ENV INFLUXDB_USERNAME ""  
ENV INFLUXDB_PASSWORD ""  
ENV MONITOR_NAME "miner_stats"  
ENV MONITOR_URL "http://miner:8080/api.json"  
ENV MONITOR_METHOD "GET"  
RUN apk add --update \  
bash \  
gettext \  
&& rm -rf /var/cache/apk/*  
  
COPY telegraf .  
COPY telegraf.conf.template .  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  

