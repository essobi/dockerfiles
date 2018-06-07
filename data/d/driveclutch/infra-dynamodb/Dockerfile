FROM driveclutch/alpine-java:1.1  
USER root  
  
RUN apk -Uuv add ca-certificates openssl groff less python py-pip && \  
wget -q http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz && \  
tar zxvf dynamodb_local_latest.tar.gz && \  
rm dynamodb_local_latest.tar.gz && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
EXPOSE 8080  
CMD ["java", "-Xmx128M", "-Xmx128M", "-jar", "DynamoDBLocal.jar", "-dbPath",
".", "--sharedDb", "-port", "8080"]  

