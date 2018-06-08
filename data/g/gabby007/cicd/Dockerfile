FROM java:8  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
COPY src /home/root/javahelloworld/src  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get update && apt-get install -y vim  
  
ENTRYPOINT ["java","-cp","bin","HelloWorld"]  

