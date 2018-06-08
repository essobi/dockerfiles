## api  
FROM nunofontes/esmachine  
MAINTAINER nuno@tradingeconomics.com  
  
# Copy supervisor  
COPY supervisord.conf /etc/  
  
# Copy settings  
COPY elasticsearch.yml /elasticsearch/config/  
COPY logging.yml /elasticsearch/config/  
  
COPY analysis/ /elasticsearch/config/analysis/  
COPY scripts/ /elasticsearch/config/scripts/  
  
CMD ["/usr/local/bin/supervisord"]  
  
EXPOSE 9200  
EXPOSE 9300

