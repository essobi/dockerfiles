FROM java:8-jdk-alpine  
  
MAINTAINER gtclai "tsungchih.hd@gmail.com"  
ENV AKKA_VERSION 2.4.3  
ENV SCALA_VERSION 2.11  
ADD http://downloads.typesafe.com/akka/akka_$SCALA_VERSION-$AKKA_VERSION.zip
/opt  
ENV CLASSPATH $CLASSPATH:/opt/akka-$AKKA_VERSION  
COPY AkkaLogParsing.jar /usr/src/showcase/  
  
EXPOSE 4001  
ENTRYPOINT ["java", "-cp", "/usr/src/showcase/AkkaLogParsing.jar",
"AkkaLogParsing.App"]  
CMD ["10.5.20.204:9772,10.5.20.206:9349,10.5.20.208:9344", "syslogEvents",
"10.5.20.206", "9042", "21600"]  

