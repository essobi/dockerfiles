FROM maven:3.5-jdk-8-slim  
  
COPY . /usr/quizduell/  
  
WORKDIR /usr/quizduell/commons/  
RUN mvn install  
  
WORKDIR /usr/quizduell/backend/  
RUN mvn install  
  
EXPOSE 8080  
CMD mvn exec:java -Dexec.args="-host http://0.0.0.0"

