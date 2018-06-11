FROM yugeshdocker1/docker-splunk-light:latest  
MAINTAINER Yugesh Avadhanula <yugesh.a@tcs.com>  
  
ADD docker.xml
${SPLUNK_BACKUP_DEFAULT_ETC}/etc/apps/search/local/data/ui/views/  
ADD docker_container.xml
${SPLUNK_BACKUP_DEFAULT_ETC}/etc/apps/search/local/data/ui/views/  
ADD inputs.conf ${SPLUNK_BACKUP_DEFAULT_ETC}/etc/apps/search/local/  

