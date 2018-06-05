FROM java:8u91-jdk  
  
# Install maven  
RUN apt-get update && \  
apt-get install -y maven  
  
WORKDIR /code  
  
# Prepare by downloading dependencies  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
# Adding source, compile and package into a fat jar  
ADD src /code/src  
  
ADD build.sh /code/build.sh  
RUN sed -i 's/\r//' /code/build.sh  
  
EXPOSE 8080  
CMD ["./build.sh"]

