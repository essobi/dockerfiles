FROM openjdk:alpine  
ENV FOO bar  
#COPY Hello.java /  
COPY src /root/java-hello/src  
WORKDIR /root/java-hello  
RUN mkdir bin  
RUN javac -d bin src/Hello.java  
  
ENTRYPOINT ["java", "-cp", "bin", "Hello"]  

