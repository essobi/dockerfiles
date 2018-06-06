FROM mrlesmithjr/ubuntu-ansible:16.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Copy Configs  
COPY config/ /  
  
# Copy Ansible Playbook  
COPY playbook.yml /playbook.yml  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml  
  
# Cleanup  
RUN apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define Environment Vars  
ENV SNORT_INT=eth0  
  
# Copy entrypoint script and make executable  
COPY docker-entrypoint.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
# Execute  
CMD ["docker-entrypoint.sh"]  

