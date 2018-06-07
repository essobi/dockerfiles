FROM gradle:4.7-jdk8-alpine  
  
RUN pwd  
COPY . /home/gradle/src  
  
RUN ls -l /home/gradle/src/  
  
WORKDIR /home/gradle/src  
RUN ls -l  
  
USER root  
RUN chmod -R 777 gradlew  
RUN ls -l  
RUN ./gradlew build  
RUN pwd  
RUN cp build/libs/corebaz-1.0.0.jar /corebaz-1.0.0.jar  
RUN ls -lrth  
RUN ls -lrth ../  
RUN ls -lrth ../../  
RUN rm -f -R *  
RUN ls -lrth  
  
USER gradle  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/corebaz-1.0.0.jar"]  

