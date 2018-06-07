#ref https://github.com/splunk/docker-splunk/blob/master/enterprise/Dockerfile  
FROM splunk/splunk:6.5.0  
LABEL description = "The Splunk App for Jenkins image"  
  
MAINTAINER Ted <txiao@splunk.com>  
  
USER splunk  
ENV package splunk-app-for-jenkins.tgz  
ENV SPLUNK_BACKUP_DEFAULT_ETC /var/opt/splunk  
  
COPY ${package} app.md5 /tmp/  
RUN cd /tmp && md5sum -c app.md5  
#deploy HTTP Event Collector token  
COPY inputs.conf ${SPLUNK_BACKUP_DEFAULT_ETC}/etc/apps/splunk_httpinput/local/  
#deploy splunk-app-for-jenkins  
RUN tar -xzf /tmp/${package} -C ${SPLUNK_BACKUP_DEFAULT_ETC}/etc/apps/  
  
#run entrypoint.sh using root  
USER root  
RUN rm /tmp/${package}  

