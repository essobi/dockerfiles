FROM lejunzhu/docker-java-opencv  
  
MAINTAINER Lejun Zhu <danielzhu28@gmail.com>  
  
RUN wget -q -O - http://d3kbcqa49mib13.cloudfront.net/spark-1.4.0-bin-
hadoop2.4.tgz | tar xzv -C /opt  
RUN ln -s /opt/spark-1.4.0-bin-hadoop2.4 /opt/spark  
  
ENTRYPOINT ["/bin/bash"]  
  

