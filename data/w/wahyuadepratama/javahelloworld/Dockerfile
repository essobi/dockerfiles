FROM java:8  
COPY src /home/student/java/javahelloworld/src  
  
WORKDIR /home/student/java/javahelloworld  
  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

