FROM java:7  
WORKDIR /home/root/javahelloworld  
#COPY ./ ./  
# more comments  
COPY src src  
RUN mkdir bin  
RUN javac -d bin src/HelloWorld.java  
# basta un entrypoint eseguirà solo il primo  
RUN echo "test"  
ENTRYPOINT ["java","-cp","bin","HelloWorld"]  

