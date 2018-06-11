FROM java:7  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
COPY src /home/root/javahelloworld/src  
RUN javac -d bin src/HelloWorld.java  
#ENTRYPOINT ["java", "HelloWorld"]  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

