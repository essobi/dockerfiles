FROM maven:3-jdk-8  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app  
  
EXPOSE 2000  
RUN cd backend && mvn -T4 clean package  
  
RUN java -jar backend/app/target/app-1.0-SNAPSHOT.jar db migrate
backend/app/studybox-h2.yml  
  
CMD ["java -jar", "backend/app/target/app-1.0-SNAPSHOT.jar server
backend/app/studybox-h2.yml"]  

