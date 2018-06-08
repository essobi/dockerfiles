FROM dockerfile/java:oracle-java7  
MAINTAINER Ganesh Ravi <ganesh.reddy.22@gmail.com>  
  
RUN apt-get -y update  
  
# Installing GIT and Maven  
RUN apt-get -y install aptitude  
  
RUN aptitude -y install git maven  
  
# Cloning the Event Filter GIT project  
RUN git clone https://GaneshRavi@bitbucket.org/GaneshRavi/filtering_engine.git  
  
WORKDIR filtering_engine  
  
RUN sed -i 's/localhost/mongohost/g' src/main/resources/eventfilter.properties  
  
# Pre-compiling it, so that the Maven dependencies are brought in during
"build", rather than during "run"  
RUN mvn compile  
  
EXPOSE 6666 6667  
CMD ["mvn", "camel:run"]  

