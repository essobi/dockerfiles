FROM openjdk:8-jdk  
MAINTAINER István Földházi <istvan.foldhazi@gmail.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV JAVA_OPTS ""  
ENV PATH $PATH:$JAVA_HOME/bin  
  
ENV TIME_ZONE Europe/Budapest  
ENV SPRING_PROFILES_ACTIVE test  
  
ENV TZ=$TIME_ZONE  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
WORKDIR /app  
  
EXPOSE 8080  
ONBUILD COPY app.jar /app/app.jar  
  
CMD ["/bin/sh", "-c", "java $JAVA_OPTS -jar /app/app.jar
--spring.profiles.active=$SPRING_PROFILES_ACTIVE"]

