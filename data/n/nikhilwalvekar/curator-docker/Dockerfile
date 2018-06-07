FROM gliderlabs/alpine:3.2  
ENV CURATOR_VERSION 5.2.0  
ENV ELASTICSEARCH_PORT 9200  
ENV INDICES_PREFIXES logstash  
ENV USE_SSL false  
  
RUN apk --update add python py-pip bash && pip install elasticsearch-
curator==$CURATOR_VERSION  
  
ADD docker-entrypoint.sh /  
ADD tasks/optimize-indices.sh /etc/periodic/  
ADD tasks/purge-old-indices.sh /etc/periodic/  
ADD config.yml /etc/periodic/config/  
ADD actions.yml /etc/periodic/config/  
  
RUN printf "\n0\t2\t*\t*\t*\t/etc/periodic/purge-old-indices.sh" >>
/etc/crontabs/root  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["crond", "-f", "-l", "8"]  

