FROM java:8  
WORKDIR /code  
  
# Adding source, compile and package into a fat jar  
ADD . /code  
RUN ["./gradlew", "build"]  
  
EXPOSE 4567  
CMD ["java", "-jar", "build/libs/LemPortService-1.0.0.jar"]

