# build: docker build -t elasticmq .  
# run: docker run --rm -v "$(pwd)/config:/elasticmq/config:ro" -p 9324:9324
elasticmq  
FROM centos:centos7  
  
EXPOSE 9324  
RUN yum install -y java-1.7.0-openjdk  
  
RUN mkdir /elasticmq && \  
cd /elasticmq && \  
curl -sS -o \  
/elasticmq/elasticmq-server-0.8.0.jar \  
https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-0.8.0.jar  
ADD run.sh /  
ADD my_logback.xml /elasticmq/  
  
CMD ["/run.sh"]  

