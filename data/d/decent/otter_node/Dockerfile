FROM openjdk:8-jre-alpine  
MAINTAINER mr5.simple@gmail.com  
  
RUN apk add -U tzdata bash file aria2  
  
RUN mkdir -p /opt/otter_node  
ADD
https://github.com/alibaba/otter/releases/download/v4.2.14/node.deployer-4.2.14.tar.gz
/opt/otter_node/  
RUN cd /opt/otter_node && tar -zxvf node.deployer-4.2.14.tar.gz && rm
node.deployer-4.2.14.tar.gz  
  
ADD docker-entrypoint.sh /  
RUN chmod +x docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

