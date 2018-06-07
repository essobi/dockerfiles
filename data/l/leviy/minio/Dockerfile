FROM minio/minio  
  
COPY entrypoint.sh /usr/bin/  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
CMD ["minio","server","/data"]  

