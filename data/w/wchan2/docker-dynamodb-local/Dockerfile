FROM ubuntu  
MAINTAINER William Chan <wchan@shopkeep.com>  
  
RUN apt-get update && apt-get install -y build-essential curl openjdk-7-jdk  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
RUN mkdir -p /opt/local  
WORKDIR cd /opt/local  
  
RUN curl -SsfOL "https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_2013-12-12.tar.gz"  
RUN tar -xvf dynamodb_local_2013-12-12.tar.gz  
  
EXPOSE 8000  
CMD ["java", "-Djava.library.path=./dynamodb_local_2013-12-12", "-jar",
"./dynamodb_local_2013-12-12/DynamoDBLocal.jar"]  

