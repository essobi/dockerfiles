FROM docker.elastic.co/beats/filebeat:6.2.2  
ADD filebeat.yml /etc/filebeat/filebeat.yml  
ADD start.sh /start.sh  
VOLUME /etc/filebeat  
CMD "/start.sh"  

