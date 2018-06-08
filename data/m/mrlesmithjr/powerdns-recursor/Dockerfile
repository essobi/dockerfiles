FROM mrlesmithjr/ubuntu-ansible:14.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
ENV PDNS_RECURSOR_LOCAL_ADDRESS="0.0.0.0" \  
PDNS_RECURSOR_LISTEN_PORT="5300"  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy entrypoint script and make executable  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
# Expose port(s)  
EXPOSE 5300 5300/udp  
  
# Execute  
CMD ["/docker-entrypoint.sh"]  

