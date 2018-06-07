FROM koda/docker-knowledge  
  
COPY ./run.sh /root/  
COPY ./custom_connection.xml /root/.knowledge/  
  
RUN chmod +x /root/run.sh  
  
CMD ["/root/run.sh"]  

