FROM openjdk:8-jre  
  
COPY entrypoint.sh /usr/local/lib/dynamodb/  
  
RUN mkdir -p /usr/local/lib/dynamodb \  
&& wget -P /tmp https://s3.eu-central-1.amazonaws.com/dynamodb-local-
frankfurt/dynamodb_local_latest.tar.gz \  
&& tar -zxvf /tmp/dynamodb_local_latest.tar.gz -C /usr/local/lib/dynamodb \  
&& chmod +x usr/local/lib/dynamodb/entrypoint.sh  
  
WORKDIR /usr/local/lib/dynamodb  
  
EXPOSE 8000  
  
ENTRYPOINT ["/usr/local/lib/dynamodb/entrypoint.sh"]  

