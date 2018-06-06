FROM bobrik/curator:latest  
  
RUN mkdir /opt/curator/files -p  
ADD entry.sh /opt/curator  
ADD files /opt/curator/files/  
  
ENTRYPOINT ["/bin/sh", "/opt/curator/entry.sh"]  

