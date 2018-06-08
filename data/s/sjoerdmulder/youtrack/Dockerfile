FROM java:8  
MAINTAINER Sjoerd Mulder <sjoerd@sagent.io>  
  
ENV YOUTRACK_VERSION 6.5.16953  
ADD https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar
youtrack-$YOUTRACK_VERSION.jar  
ADD
https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar.sha256
youtrack-$YOUTRACK_VERSION.jar.sha256  
  
RUN sha256sum -c youtrack-$YOUTRACK_VERSION.jar.sha256  
  
EXPOSE 8080  
VOLUME /data/youtrack  
  
CMD ["java", "-Xmx1g", "-XX:MaxMetaspaceSize=250m",
"-Djava.awt.headless=true", "-Ddatabase.location=/data/youtrack", "-jar",
"youtrack-6.5.16953.jar", "8080"]  

