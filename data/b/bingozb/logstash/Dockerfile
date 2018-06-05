# https://github.com/elastic/logstash-docker  
FROM docker.elastic.co/logstash/logstash-oss:6.2.2  
MAINTAINER bingo <bingov5@icloud.com>  
  
ENV LS_JAVA_OPTS "-Xmx256m -Xms256m"  
ADD https://raw.githubusercontent.com/bingozb/docker-
logstash/master/logstash.yml /usr/share/logstash/config/logstash.yml  
ADD https://raw.githubusercontent.com/bingozb/docker-
logstash/master/logstash.conf /usr/share/logstash/pipeline/logstash.conf  
  
USER root  
  
RUN chown -R logstash:logstash /usr/share/logstash/config \  
&& chown -R logstash:logstash /usr/share/logstash/pipeline  
  
USER logstash  
  
EXPOSE 5000

