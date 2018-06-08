FROM java  
MAINTAINER Docker Training <mool@bit>  
  
ENV FOO bar  
  
WORKDIR /home/root/javahelloworld  
COPY /src src  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
RUN echo "This is another RUN line"  
  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
  

