FROM frekele/maven  
MAINTAINER ekrem@xellucia.org  
  
COPY . /app  
WORKDIR /app  
  
RUN mvn clean compile package  
  
WORKDIR /app/target  
  
ENV JAVA_OPTS=""  
ENV MONGO_HOST=""  
ENV RABBIT_HOST=""  
EXPOSE 8080:8080  
CMD java -jar JobHandling-0.0.1-SNAPSHOT.jar

