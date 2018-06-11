FROM java:7  
ENV FOO bar  
RUN apt-get update && apt-get install -y vim  
COPY src/HelloWorld.java /home/root/javahelloworld/src/HelloWorld.java  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
#RUN /usr/bin/javac -d /home/root/javahelloworld/bin
/home/root/javahelloworld/src/HelloWorld.java  
RUN /usr/bin/javac -d bin src/HelloWorld.java  
ENV OH NO  
ENTRYPOINT ["java","-cp","/home/root/javahelloworld/bin","HelloWorld"]  
  

