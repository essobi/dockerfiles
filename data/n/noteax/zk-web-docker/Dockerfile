FROM openjdk:8  
MAINTAINER Aidar Bariev <aidarbariev@gmail.com>  
  
ENV ZKWEB_PORT=8080  
ENV ZKWEB_CREDENTIALS=admin:hello  
ENV ZKWEB_DEFAULT_NODE=localhost:2181  
RUN wget -q "https://github.com/noteax/zk-web/releases/download/v.1.1.0/zk-
web-1.1.0-standalone.jar"  
  
EXPOSE $ZKWEB_PORT  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["java", "-jar", "zk-web-1.1.0-standalone.jar"]

