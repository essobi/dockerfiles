FROM postgres:9.6  
RUN apt-get update && apt-get install s3cmd -y  
  
ADD ./restore.sh /usr/local/bin  
  
CMD ["restore.sh"]  

