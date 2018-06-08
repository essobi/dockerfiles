FROM minio/minio  
  
ADD dev-bucket /tmp/dev-bucket  
  
ENV MINIO_ACCESS_KEY=minio-access  
ENV MINIO_SECRET_KEY=minio-secret  
  
ADD entrypoint.sh .  
RUN chmod +x entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["server","/export"]  

