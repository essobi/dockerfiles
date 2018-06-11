FROM java:8  
COPY src /home/root/javahelloworld/src  
RUN javac -d bin /home/root/javahelloworld/src/HelloWorld.java  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

