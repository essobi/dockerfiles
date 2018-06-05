FROM java:8  
ARG USER=root  
  
WORKDIR /home/$USER/javahelloworld  
  
COPY src src  
  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

