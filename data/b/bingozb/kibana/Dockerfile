# https://github.com/elastic/kibana-docker  
FROM docker.elastic.co/kibana/kibana-oss:6.2.2  
MAINTAINER bingo <bingov5@icloud.com>  
  
ADD https://raw.githubusercontent.com/bingozb/docker-kibana/master/kibana.yml
/usr/share/kibana/config/kibana.yml  
  
USER root  
  
RUN chown -R kibana:kibana /usr/share/kibana/config/  
  
USER kibana  
  
EXPOSE 5601

