FROM openjdk:8u141-jdk as builder  
COPY . /code  
WORKDIR /code  
RUN ./sbt dist  
RUN mkdir /tmp/app  
RUN unzip -d "/tmp/app" /code/target/universal/*.zip  
RUN mkdir /app  
RUN mv /tmp/app/*/* /app/  
  
FROM openjdk:8u141-jre  
COPY \--from=builder /app /app  
WORKDIR /app  
CMD ["./bin/chorekiller"]  

