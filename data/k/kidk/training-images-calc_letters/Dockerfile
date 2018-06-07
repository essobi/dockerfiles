FROM openjdk:8  
MAINTAINER Frederick Ryckbosch <fred@coscale.com>  
  
ENV DATABASE_HOST database  
ENV DATABASE_USER root  
ENV DATABASE_PASS secret  
ENV DATABASE_TABLE my_db  
ENV REDIS_HOST redis  
  
COPY java-code /opt/calc-letters  
  
RUN apt-get update && apt-get install -y maven && \  
cd /opt/calc-letters && mvn package  
  
WORKDIR /opt/calc-letters/target/  
CMD [ "java", "-cp", "calc-letters-1.0-SNAPSHOT-jar-with-dependencies.jar",
"-Dcom.sun.management.jmxremote",
"-Dcom.sun.management.jmxremote.authenticate=false",
"-Dcom.sun.management.jmxremote.port=9100",
"-Dcom.sun.management.jmxremote.ssl=false", "com.coscale.App" ]  
  
LABEL
com.coscale.monitoring='[{"PluginType":"JMX","Configuration":{"BEANS":[],"METRIC":[],"JMX
HOSTNAME":["localhost"],"JMX PORT":["9100"],"COLLECT JVM":["true"]}}]'  

