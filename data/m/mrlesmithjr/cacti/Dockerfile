FROM mrlesmithjr/ubuntu-ansible:14.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
ENV CACTI_VERSION="0.8.8h" \  
CACTI_DB="cactidb" \  
CACTI_DB_HOST="db" \  
CACTI_DB_PASSWORD="cacti" \  
CACTI_DB_USER="cactiuser" \  
CACTI_USER="cactiuser" \  
CACTI_USER_PASSWORD="cacti"  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml \  
\--extra-vars "cacti_version=$CACTI_VERSION cacti_db=$CACTI_DB \  
cacti_db_host=$CACTI_DB_HOST cacti_db_user=$CACTI_DB_USER \  
cacti_db_password=$CACTI_DB_PASSWORD cacti_user=$CACTI_USER \  
cacti_user_password=$CACTI_USER_PASSWORD" && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Volume to hold config and checks  
VOLUME /config  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY config/supervisord/*.conf /etc/supervisor/conf.d/  
  
# Expose ports  
EXPOSE 80 443  

