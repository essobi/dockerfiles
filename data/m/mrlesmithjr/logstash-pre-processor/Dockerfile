FROM mrlesmithjr/logstash:latest  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Define Environment Variables  
ENV REDIS_SERVER="redis"  
# Copy new configurations  
COPY config/logstash/ /etc/logstash/conf.d  
  
# Copy Ansible Files  
COPY config/ansible/ /  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Expose ports  
EXPOSE 2055/udp 5044 10514 10514/udp  

