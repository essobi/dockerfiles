FROM mrlesmithjr/alpine-ansible  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
RUN ansible-playbook -i "localhost," -c local /playbook.yml && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
ENV POSTFIX_CONF_DIR="/etc/postfix" \  
POSTFIX_MYNETWORKS="127.0.0.0/8"  
# Setup volumes  
VOLUME ["/var/lib/postfix", "/var/mail", "/var/spool/postfix"]  
  
COPY config/supervisord/*.ini /etc/supervisor.d/  
  
# Expose ports  
EXPOSE 25  

