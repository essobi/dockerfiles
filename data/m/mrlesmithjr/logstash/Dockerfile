FROM ubuntu:14.04  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
# Update apt-cache  
RUN apt-get update  
  
# Install Ansible  
RUN apt-get -y install git software-properties-common && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get -y install ansible  
  
# Copy Ansible Playbook  
COPY playbook.yml /playbook.yml  
  
# Run Ansible playbook  
RUN ansible-playbook -i "localhost," -c local /playbook.yml  
  
# Cleanup  
RUN apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH /opt/logstash/bin:$PATH  
  
# necessary for 5.0+ (overriden via "--path.settings", ignored by < 5.0)  
ENV LS_SETTINGS_DIR /etc/logstash  
# comment out some troublesome configuration parameters  
# path.log: logs should go to stdout  
# path.config: No config files found: /etc/logstash/conf.d/*  
RUN set -ex \  
&& if [ -f "$LS_SETTINGS_DIR/logstash.yml" ]; then \  
sed -ri 's!^(path.log|path.config):!#&!g' "$LS_SETTINGS_DIR/logstash.yml"; \  
fi  
  
# Setup entrypoint Ansible Playbook  
COPY docker-entrypoint.yml /docker-entrypoint.yml  
  
# Setup entrypoint script  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
COPY config/ /etc/logstash/conf.d  
  
# Setup volume  
VOLUME /etc/logstash/conf.d  
  
# Expose Port(s)  
EXPOSE 514 514/udp 5044 10514 10514/udp  
  
# Container start-up  
CMD ["logstash", "agent", "-f", "/etc/logstash/conf.d/"]  

