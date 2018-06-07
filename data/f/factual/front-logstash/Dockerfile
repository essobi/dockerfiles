FROM logstash:5  
RUN logstash-plugin install logstash-input-beats  
RUN logstash-plugin install logstash-output-file  
  
RUN apt-get update  
RUN apt-get install -y s3cmd ruby logrotate  
  
ADD bin/* /usr/local/bin/  
  
ENTRYPOINT []  
CMD [ "bootstrap" ]  

