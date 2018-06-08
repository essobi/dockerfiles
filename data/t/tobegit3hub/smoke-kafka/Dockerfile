FROM java  
MAINTAINER tobe tobeg3oogle@gmail.com  
  
RUN apt-get -y update  
  
# Install tools  
RUN apt-get install -y maven  
  
# Add code  
ADD . /smoke-kafka  
WORKDIR /smoke-kafka  
  
RUN mvn clean package  
  
# Start kafka  
CMD sh ./target/smoke-kafka-1.0-SNAPSHOT/bin/smoke-kafka.sh  

