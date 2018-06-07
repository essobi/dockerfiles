FROM alpine:latest  
  
ENV ELASTICSEARCH_PORT 9200  
ENV ELASTICSEARCH_HOST elasticsearch  
ENV INDICES_PREFIXES logstash  
ENV MAX_INDEX_AGE 7  
RUN apk --update add python py-pip bash && pip install elasticsearch-curator  
  
ADD docker-entrypoint.sh /  
COPY action.yml /  
COPY config.yml /  
#Have to remove the .sh for run-parts...  
COPY expire-indices.sh /etc/periodic/daily/expire-indices  
RUN chmod a+x /etc/periodic/daily/expire-indices  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["crond", "-f", "-l", "8"]  

