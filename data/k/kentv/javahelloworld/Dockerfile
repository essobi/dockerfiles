FROM java:7  
COPY src /home/root/javahelloworld/src  
ENV nisse kalle  
RUN mkdir /home/root/javahelloworld/bin && cd /home/root/javahelloworld &&
javac -d bin src/HelloWorld.java  
ENTRYPOINT ["java", "-cp", "/home/root/javahelloworld/bin", "HelloWorld"]  
  

