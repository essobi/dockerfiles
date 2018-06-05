FROM ruby:2.3.3-alpine  
MAINTAINER Per Christian B. Viken <perchr@northblue.org>  
  
RUN addgroup -S batsd && adduser -S -D -s /bin/false -G batsd -g batsd batsd  
  
RUN gem update --system && gem install bundler  
RUN apk add --no-cache --virtual build-dependencies build-base  
RUN apk update && apk add ca-certificates openssl redis supervisor procmail
ssmtp  
RUN mkdir -p /app \  
&& wget -O - https://github.com/PerfectlyNormal/batsd/archive/master.tar.gz \  
| tar -xz -C /app \  
&& chown -R batsd:batsd /app \  
&& cd /app \  
&& find batsd-master -name ".*" -mindepth 1 -maxdepth 1 -exec mv {} . \; \  
&& mv batsd-master/* . && rmdir batsd-master \  
&& bundle install  
  
RUN mkdir -p /data/batsd /data/redis \  
&& chown -R batsd:batsd /data/batsd \  
&& chown -R redis:redis /data/batsd \  
&& chmod 700 /data/  
VOLUME /data  
  
ADD etc/hourly-truncate /etc/periodic/hourly/batsd-truncate  
ADD etc/daily-truncate /etc/periodic/daily/batsd-truncate  
RUN chmod +x /etc/periodic/hourly/batsd-truncate /etc/periodic/daily/batsd-
truncate  
  
ADD etc/config.yml /app/config.yml  
ADD etc/redis.conf /etc/redis.conf  
ADD etc/supervisord.conf /etc/supervisord.conf  
RUN mkdir /var/log/supervisor  
  
WORKDIR /app  
  
EXPOSE 8125/udp 8126 8127  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]

