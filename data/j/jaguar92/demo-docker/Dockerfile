FROM java:8  
RUN mkdir /mydir  
ENV HOSTNAME mycontainer  
COPY target/demo-0.0.1-SNAPSHOT.jar /mydir  
WORKDIR /mydir  
EXPOSE 8080  
CMD ["java","-jar","demo-0.0.1-SNAPSHOT.jar"]  

