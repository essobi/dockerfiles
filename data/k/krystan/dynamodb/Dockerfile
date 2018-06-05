  
FROM openjdk:8u151-jre-slim-stretch  
  
MAINTAINER Krystan Honour <github.com/krystan>  
  
WORKDIR /opt/dynamodb_local  
  
RUN mkdir -p /opt/dynamodb_local \  
mkdir -p /home/dynamodb \  
mkdir -p /dynamodb_local_db  
  
RUN groupadd -g 999 dynamodb \  
&& useradd -r -u 999 -g dynamodb dynamodb \  
&& mkdir -p /home/dynamodb \  
&& chown -R dynamodb:dynamodb /home/dynamodb \  
&& chown -R dynamodb:dynamodb /opt/dynamodb_local \  
&& chown -R dynamodb:dynamodb /dynamodb_local_db  
  
RUN apt-get update -y \  
&& apt-get install wget -y \  
&& wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest.tar.gz -q -O - | tar -xz \  
&& apt-get purge --auto-remove -y wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
VOLUME ["/dynamodb_local_db"]  
  
EXPOSE 8000  
# run non root  
USER dynamodb  
  
ENTRYPOINT ["java", "-jar", "DynamoDBLocal.jar"]  
  
CMD ["--sharedDb", "-inMemory", "-port", "8000"]  

