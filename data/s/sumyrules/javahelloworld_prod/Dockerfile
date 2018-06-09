FROM java:7  
ENV FOO bar  
COPY src /home/root/javahelloworld/src  
WORKDIR /home/root/javahelloworld  
RUN mkdir bin  
RUN mkdir testing  
RUN javac -d bin src/helloworld.java  
ENTRYPOINT ["java","-cp","bin","helloworld"]  
  

