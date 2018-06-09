FROM java:7  
WORKDIR /home/root/javahelloworld  
COPY src src  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN touch a  
RUN touch b  
ENTRYPOINT ["java","-cp","bin","HelloWorld"]  
  

