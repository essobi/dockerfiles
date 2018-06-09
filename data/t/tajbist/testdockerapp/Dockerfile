FROM java:9  
COPY ./src/main/java/ /src/main/java  
WORKDIR /src/main/java  
LABEL vendorl="testdock"  
#ADD . /src/main/java  
RUN javac Hello.java  
CMD ["java","Hello"]  
  
#ADD . /usr/local/helloworld  
#RUN cd /usr/local/helloworld && mvn install  
#CMD ["java", "-cp", "/usr/local/helloworld/target/helloworld-1.0.jar",
"HelloWorld"]  

