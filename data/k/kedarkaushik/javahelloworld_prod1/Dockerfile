FROM java:7  
COPY HelloWorld.java /  
RUN javac HelloWorld.java  
#COPY src /home/root/javahelloworld/src  
#WORKDIR /home/root/javahelloworld  
#RUN mkdir bin  
#RUN javac -d bin src/HelloWorld.java  
RUN apt-get update && apt-get install -y vim  
ENTRYPOINT ["java", "HelloWorld"]  

