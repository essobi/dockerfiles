FROM ubuntu:12.04  
  
COPY . /src  
  
RUN apt-get update && apt-get install -y openjdk-7-jdk maven && cd /src && mvn
clean package && rm -rf /var/lib/apt/lists/*  
  
CMD cd /src && java $JAVA_OPTS -jar lib/tomee-embedded-1.1.0-SNAPSHOT-uber.jar
\--port $PORT \--path target/*.war \--context /  

