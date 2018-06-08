FROM java:7  
COPY src /root/HelloWorld/src  
WORKDIR /root/HelloWorld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN echo toto  
ENTRYPOINT ["java","-cp","bin","HelloWorld"]  
  

