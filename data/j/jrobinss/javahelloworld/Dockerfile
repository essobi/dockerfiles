FROM java:8  
MAINTAINER Julien Robinson jrobinss  
RUN mkdir javahelloworld  
WORKDIR javahelloworld  
RUN mkdir src  
RUN mkdir bin  
COPY src/HelloWorld.java src/  
RUN javac -d bin src/HelloWorld.java  
ENV FOO bar  
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]  
RUN echo "toto" > toto  

