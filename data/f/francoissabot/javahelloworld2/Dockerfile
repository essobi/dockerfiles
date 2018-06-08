FROM java:8  
ENV FOO bar  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN touch toto && touch tata  
ENTRYPOINT java -cp bin HelloWorld  
  

