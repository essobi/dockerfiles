# Training Docker File : "Dockeriser" une appli Java  
#FROM ubuntu:16.10  
FROM java:7  
COPY HelloWorld.java /opt/javaapp/src/  
  
WORKDIR /opt/javaapp  
  
RUN mkdir bin  
  
RUN javac -d bin src/HelloWorld.java  
  
ENTRYPOINT ["java", "-cp", "bin"]  
  
CMD ["HelloWorld"]  

