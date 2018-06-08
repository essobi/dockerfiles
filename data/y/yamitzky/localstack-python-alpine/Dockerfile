FROM python:3.6-alpine  
  
ENV SERVICES=apigateway,lambda,cloudformation,dynamodbstreams,firehose,s3,sns  
  
RUN apk add --no-cache --virtual build-essentials \  
gcc \  
linux-headers && \  
apk add --no-cache \  
musl-dev \  
libffi-dev \  
openssl-dev  
  
RUN pip install localstack  
  
RUN apk del --purge build-essentials  
  
EXPOSE 4567-4583 8080  
VOLUME /tmp/localstack  
  
ENTRYPOINT ["localstack"]  
  
CMD ["start"]  

