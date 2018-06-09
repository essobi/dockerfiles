FROM ubuntu:latest  
  
MAINTAINER TSUYOSHI TORII toritori0318  
  
# install add-apt-repository  
RUN apt-get update \  
&& apt-get install -y python-software-properties software-properties-common
wget  
  
# source  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
  
# java  
RUN apt-get update \  
&& apt-get install oracle-java7-installer -y \  
&& apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# dynamodb-local  
RUN wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest -O dynamo.tar.gz  
RUN mkdir dynamodb_local  
RUN tar xvzf dynamo.tar.gz -C ./dynamodb_local && rm -f dynamo.tar.gz  
  
EXPOSE 8000  
CMD ["java", "-Djava.library.path=./dynamodb_local/DynamoDBLocal_lib", "-jar",
"./dynamodb_local/DynamoDBLocal.jar"]  

