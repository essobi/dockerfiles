FROM centos:7  
RUN yum -y upgrade && \  
yum -y install curl  
  
ENV JAVA_VERSION=8 \  
JAVA_UPDATE=66 \  
JAVA_BUILD=17 \  
JAVA_START_HEAP=32m \  
JAVA_MAX_HEAP=512m \  
LOG_LEVEL="INFO"  
RUN curl -LO -H "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.rpm"
&& \  
yum -y install jq "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.rpm"
https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-
agent-1.0-1.amzn1.noarch.rpm && \  
rm -f "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.rpm"  
  
COPY agent.json /etc/aws-kinesis/agent.json  
  
CMD /usr/bin/start-aws-kinesis-agent -L $LOG_LEVEL -l /dev/stdout  

