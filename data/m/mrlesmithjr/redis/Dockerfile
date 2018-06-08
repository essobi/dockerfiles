FROM mrlesmithjr/alpine-ansible  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY config/supervisord/*.ini /etc/supervisor.d/  
  
VOLUME /data  
  
# Expose ports  
EXPOSE 6379  

