FROM mrlesmithjr/ubuntu-ansible:14.04  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Define environment variables  
ENV PDNS_ALLOW_DDNS_UPDATE="yes" \  
PDNS_ALLOW_DDNS_UPDATE_FROM="0.0.0.0/0" \  
PDNS_API_KEY="changeme" \  
PDNS_GMYSQL_DBNAME="powerdns" \  
PDNS_GMYSQL_HOST="pdns-db" \  
PDNS_GMYSQL_PASSWORD="powerdns" \  
PDNS_GMYSQL_USER="powerdns" \  
PDNS_JSON_INTERFACE="yes" \  
PDNS_LOG_DNS_QUERIES="yes" \  
PDNS_RECURSOR_SERVER="pdns-recursor" \  
PDNS_RECURSOR_SERVER_PORT="5300" \  
PDNS_WEBSERVER_ADDRESS="0.0.0.0" \  
PDNS_WEBSERVER_PASSWORD="changeme" \  
PDNS_WEBSERVER_PORT="8081" \  
PDNS_WEBSERVER="yes"  
# Copy entrypoint script and make executable  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
# Expose port(s)  
EXPOSE 53 53/udp 8081  
# Execute  
CMD ["/docker-entrypoint.sh"]  

