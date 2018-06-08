FROM mrlesmithjr/logstash:latest  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Define Environment Variables  
ENV ES_SERVER="http://elasticsearch:9200" \  
REDIS_SERVER="redis"  
# Copy new configurations  
COPY config/logstash/ /etc/logstash/conf.d  
  
# Copy Ansible Files  
COPY config/ansible/ /  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

