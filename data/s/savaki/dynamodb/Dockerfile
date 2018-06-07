FROM ubuntu:16.04  
MAINTAINER Matt Ho <matt.ho@gmail.com>  
  
ENV UPDATED_AT Sun Sep 3 19:15:05 PDT 2017  
#  
# Install Java 8  
#  
#---------------------------------------------------------------------------  
RUN apt-get -yqq update  
RUN apt-get -yqq install software-properties-common python-software-properties  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN mkdir /opt/dynamodb  
WORKDIR /opt/dynamodb  
  
#  
# Install DynamoDB  
#  
#---------------------------------------------------------------------------  
RUN wget -q -O - https://s3-us-west-2.amazonaws.com/dynamodb-
local/dynamodb_local_latest.tar.gz | tar -xzf - -C /opt/dynamodb  
  
EXPOSE 8000  
ENTRYPOINT ["/usr/bin/java",
"-Djava.library.path=/opt/dynamodb/DynamoDBLocal_lib", "-jar",
"DynamoDBLocal.jar", "-sharedDb"]  

