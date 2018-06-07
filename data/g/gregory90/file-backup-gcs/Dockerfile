FROM google/cloud-sdk  
  
RUN mkdir /backup  
  
ADD run /app/run  
ADD restore /app/restore  
  
RUN chmod +x /app/run  
RUN chmod +x /app/restore  

