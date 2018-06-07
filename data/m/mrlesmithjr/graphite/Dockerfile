FROM mrlesmithjr/apache2:ubuntu-16.04  
# Copy Ansible Related Files  
COPY config/ansible/ /  
  
# Run Ansible Playbook  
RUN ansible-playbook -i "localhost," -c local /graphite.yml && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Copy SupervisorD Configurations  
COPY config/supervisord/*.conf /etc/supervisor/conf.d/  
  
# Setup Volume For Graphite Data  
VOLUME /var/lib/graphite/whisper  
# Expose Ports  
EXPOSE 2003 2003/udp 2004 7002  

