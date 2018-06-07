FROM centos:7  
RUN yum clean all && \  
yum -y upgrade && \  
yum -y install curl  
  
ENV LOG_LEVEL="INFO"  
RUN yum -y install https://s3.amazonaws.com/streaming-data-agent/aws-kinesis-
agent-latest.amzn1.noarch.rpm  
  
CMD /usr/bin/start-aws-kinesis-agent -L $LOG_LEVEL -l /var/log/aws-kinesis-
agent/aws-kinesis-agent.log  
  

