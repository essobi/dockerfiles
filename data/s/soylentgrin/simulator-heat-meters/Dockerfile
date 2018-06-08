FROM fedora:22  
ENV APP_DIR=/simulator-heat-meters  
ENV APP_JAR=simulator-heat-meters-1.0-SNAPSHOT-jar-with-dependencies.jar  
  
RUN dnf install -y java-1.8.0-openjdk-headless && dnf clean all  
  
WORKDIR $APP_DIR  
  
ADD target/$APP_JAR $APP_JAR  
  
CMD java -jar $APP_JAR  

