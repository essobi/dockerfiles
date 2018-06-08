FROM mrlesmithjr/alpine-ansible  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Define Kibana version to install  
ENV KIBANA_MAJOR_VER="5.2" \  
KIBANA_VER="5.2.2"  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml \  
\--extra-vars "kibana_major_ver=$KIBANA_MAJOR_VER kibana_ver=$KIBANA_VER" && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
ENV PATH /opt/kibana/bin:$PATH  
  
# Expose port(s)  
EXPOSE 5601  
# Container start-up  
CMD ["kibana"]  

