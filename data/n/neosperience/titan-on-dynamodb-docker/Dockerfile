FROM ubuntu:16.04  
MAINTAINER Diego Ferri <diego.ferri@looptribe.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y git zip curl netcat default-jdk maven  
  
WORKDIR /opt  
  
RUN git clone https://github.com/awslabs/dynamodb-titan-storage-backend.git  
  
WORKDIR /opt/dynamodb-titan-storage-backend  
  
RUN mvn install  
  
RUN src/test/resources/install-gremlin-server.sh  
  
COPY dynamodb-local-installer.sh .  
  
RUN /bin/bash -c ./dynamodb-local-installer.sh  
  
WORKDIR /opt/dynamodb-titan-storage-backend/server/dynamodb-titan100-storage-
backend-1.0.0-hadoop1  
  
COPY gremlin-server-local.yaml conf/gremlin-server/  
  
COPY entrypoint.sh .  
  
EXPOSE 8182 8183 8184  
CMD ["./entrypoint.sh"]

