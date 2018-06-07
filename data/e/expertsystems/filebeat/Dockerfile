FROM centos:7  
# Delete CentOS installation log  
RUN rm -Rf /var/log/anaconda  
  
# Install Filebeat  
# See https://www.elastic.co/downloads/beats/filebeat for current version  
RUN curl -LO
https://download.elastic.co/beats/filebeat/filebeat-1.1.0-x86_64.rpm && \  
yum localinstall -y filebeat-1.1.0-x86_64.rpm && \  
rm -f filebeat-1.1.0-x86_64.rpm && \  
yum clean all && \  
rm -f /var/log/yum.log  
  
# Copy configuration file  
COPY filebeat.yml /etc/filebeat/  
  
# Copy entrypoint script  
COPY docker-entrypoint.sh /  
  
# Declare log directory as volumes, for use of --volumes-from  
VOLUME ["/var/log"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["filebeat", "-e"]  

