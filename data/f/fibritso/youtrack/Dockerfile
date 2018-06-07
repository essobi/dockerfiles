FROM java:8  
MAINTAINER Hanat <fibritso@gmail.com>  
  
ENV YOUTRACK_VERSION 7.0.29566  
ADD https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar
youtrack-$YOUTRACK_VERSION.jar  
ADD
https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar.sha256
youtrack-$YOUTRACK_VERSION.jar.sha256  
  
RUN sha256sum -c youtrack-$YOUTRACK_VERSION.jar.sha256  
  
RUN ln -s youtrack-$YOUTRACK_VERSION.jar youtrack.jar  
  
EXPOSE 8080  
VOLUME /data/youtrack  
  
CMD ["java", "-Xmx1g", "-XX:MaxMetaspaceSize=250m",
"-Djava.awt.headless=true", "-Ddatabase.location=/data/youtrack", "-jar",
"youtrack.jar", "8080"]

