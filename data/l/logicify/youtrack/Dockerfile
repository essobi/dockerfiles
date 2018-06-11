FROM logicify/java8  
MAINTAINER Dmitry Berezovsky <dmitry.berezovsky@logicify.com>  
  
ENV VERSION=6.5.16392  
RUN curl -L http://download-cf.jetbrains.com/charisma/youtrack-${VERSION}.jar
-o /srv/youtrack.jar  
  
EXPOSE 8080  
WORKDIR /srv  
  
USER app  
  
CMD ["java", "-Xmx1g", "-XX:MaxPermSize=250m", "-Djava.awt.headless=true",
"-jar", "youtrack.jar", "8080"]  
  
VOLUME /home/app  

