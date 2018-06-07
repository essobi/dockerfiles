# Version: 0.0.1  
FROM nimmis/java-centos:openjdk-8-jdk  
  
MAINTAINER Jonathan Creasy "jonathan.creasy@gmail.com"  
ENV JAVA_HOME /usr/lib/jvm/java  
ENV WORKDIR = /opt/instrumentation  
ENV JARNAME = instrumentation-all-1.0-SNAPSHOT.jar  
  
RUN mkdir $WORKDIR  
WORKDIR $WORKDIR  
  
ADD build\libs\$JARNAME $WORKDIR  
  
CMD ["java", "-jar", "$JARNAME"]

