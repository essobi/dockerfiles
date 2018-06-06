FROM mrlesmithjr/ubuntu-ansible:16.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
ENV RANCHER_ACCESS_KEY="" \  
RANCHER_HOST="" \  
RANCHER_HOST_PORT="8080" \  
RANCHER_PROJECT_ID="1a5" \  
RANCHER_SECRET_KEY="" \  
RANCHER_SERVICE_NAME="" \  
RANCHER_STACK_NAME=""  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY config/rancher-gen/ /etc/  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 53 53/udp  

