FROM java:8  
RUN mkdir /app  
#COPY ./build/libs/project3.jar /app/app.jar  
COPY ./ /app/  
RUN cd /app && ./gradlew build  
  
CMD ["java", "-jar", "/app/build/libs/project3.jar"]  

