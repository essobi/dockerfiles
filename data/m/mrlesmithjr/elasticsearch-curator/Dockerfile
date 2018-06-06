FROM mrlesmithjr/ubuntu-ansible:16.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Define Curator version to install  
ENV CURATOR_MAJOR_VER="4" \  
CURATOR_VER="4.1.0" \  
ELASTICSEARCH_HOST="elasticsearch" \  
DELETE_OLDER_THAN_IN_DAYS="30"  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml \  
\--extra-vars "curator_major_ver=$CURATOR_MAJOR_VER curator_ver=$CURATOR_VER"
&& \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY config/supervisord/*.conf /etc/supervisor/conf.d/  
  
# Expose ports  

