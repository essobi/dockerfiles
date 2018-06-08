FROM anapsix/alpine-java:8_jdk  
  
WORKDIR /opt  
  
ENV LC_ALL=C  
ENV MONGO_URI=mongodb://localhost:27017  
ENV RABBIT_HOST=localhost  
ENV RABBIT_PORT=5672  
# copy in the gradlew, gradle credentials and src folder  
ADD gradle ./gradle  
ADD src ./src  
  
COPY gradlew gradle.properties.enc build.gradle ./  
# build the code  
RUN java -version  
RUN ./gradlew assemble  
  
CMD java -jar build/libs/*.jar --spring.data.mongodb.uri=$MONGO_URI
\--spring.rabbitmq.host=$RABBIT_HOST \--spring.rabbitmq.port=$RABBIT_PORT  

