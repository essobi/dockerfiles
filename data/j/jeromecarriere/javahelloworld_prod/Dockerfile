FROM java:8  
ENV FOO bar  
  
#COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN touch test3  
RUN touch test1  
RUN touch test  
#RUN javac -d bin src/HelloWorld.java  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  

