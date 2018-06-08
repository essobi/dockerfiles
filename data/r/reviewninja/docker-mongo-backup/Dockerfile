FROM mongo  
  
RUN apt-get update && apt-get install -y cron  
  
ADD backup.sh /backup.sh  
ADD cronstart.sh /cronstart.sh  
ADD remove.sh /remove.sh  
ADD test.sh /test.sh  
  
RUN cd /  
  
RUN chmod +x /backup.sh  
RUN chmod +x /cronstart.sh  
RUN chmod +x /remove.sh  
RUN chmod +x /test.sh  
RUN mkdir /mongobackup  
RUN ./cronstart.sh  
  
VOLUME /mongobackup  
  
CMD ["cron", "-f"]  

