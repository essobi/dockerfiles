FROM java:8  
ENV FOO bin  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir ${FOO}  
RUN javac -d bin src/HelloWorld.java  
RUN apt-get update && apt-get install -y vim  
ENTRYPOINT ["java", "-cp","bin", "HelloWorld"]  

