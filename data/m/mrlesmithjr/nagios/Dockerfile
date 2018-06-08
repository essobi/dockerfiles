FROM mrlesmithjr/ubuntu-ansible:16.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Copy Ansible Playbook  
COPY playbook.yml /playbook.yml  
  
# Setup Environment Vars  
ENV NAGIOSADMIN_USERNAME="nagiosadmin" \  
NAGIOSADMIN_PASSWORD="nagiosadmin" \  
NAGIOS_VER="4.2.1" \  
NAGIOS_PLUGINS_VER="2.1.2"  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml \  
\--extra-vars "nagiosadmin_password=$NAGIOSADMIN_PASSWORD \  
nagiosadmin_username=$NAGIOSADMIN_USERNAME \  
nagios_ver=$NAGIOS_VER nagios_plugins_ver=$NAGIOS_PLUGINS_VER"  
  
# Cleanup  
RUN apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy Docker Entrypoint  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# Expose ports  
EXPOSE 80 443  

