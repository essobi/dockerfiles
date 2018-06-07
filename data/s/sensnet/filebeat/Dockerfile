FROM watsco/filebeat:latest  
  
COPY filebeat.yml /etc/filebeat/filebeat.yml  
  
# https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-command-
line.html  
CMD [ "filebeat", "-e", "-c", "/etc/filebeat/filebeat.yml" ]

