FROM java:8  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir /home/root/javahelloworld/bin  
RUN javac -d bin src/HelloWorld.java  
  
ENTRYPOINT ["java","-cp", "bin", "HelloWorld"]  

