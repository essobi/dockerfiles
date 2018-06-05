FROM java:7  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
ENV EMBULK_VERSION 0.4.1  
RUN curl -L
https://bintray.com/artifact/download/embulk/maven/embulk-${EMBULK_VERSION}.jar
-o /opt/embulk.jar  
  
WORKDIR /work  
ENTRYPOINT ["java", "-jar", "/opt/embulk.jar"]  
CMD ["--help"]  
  

