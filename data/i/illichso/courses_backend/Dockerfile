FROM openjdk  
  
WORKDIR courses  
  
COPY src/ src/  
COPY build.gradle ./  
COPY gradle/ gradle/  
COPY gradlew ./  
  
RUN chmod +x ./gradlew  
  
RUN ./gradlew clean build  
  
EXPOSE 8080  
ENTRYPOINT ["java", \  
"-Dspring.data.mongodb.uri=mongodb://db/courses", \  
"-Djava.security.egd=file:/dev/./urandom", \  
"-jar", \  
"build/libs/courses.jar"]

