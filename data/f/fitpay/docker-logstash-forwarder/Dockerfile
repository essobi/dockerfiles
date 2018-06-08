FROM fitpay/docker-java  
  
RUN yum install -y wget  
RUN wget https://download.elastic.co/beats/filebeat/filebeat-1.1.0-x86_64.rpm  
RUN rpm -vi filebeat-1.1.0-x86_64.rpm  
  
ADD filebeat.yml /etc/filebeat/filebeat.yml  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
CMD ["/run.sh"]  

