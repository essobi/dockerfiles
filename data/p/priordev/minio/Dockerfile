FROM ubuntu:trusty  
  
RUN mkdir -p /opt/minio/data  
ADD ./minio /opt/minio/minio  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /opt/minio/minio && \  
chmod +x /entrypoint.sh  
  
WORKDIR /opt/minio  
  
EXPOSE 9000  
VOLUME /opt/minio/data  
  
CMD [ "/entrypoint.sh" ]

