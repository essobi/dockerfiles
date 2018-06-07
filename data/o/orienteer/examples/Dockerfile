FROM orienteer/orienteer:latest  
  
RUN mkdir -p /usr/src/orienteer-examples/  
WORKDIR /usr/src/orienteer-examples/  
ADD . /usr/src/orienteer-examples/  
RUN mvn clean install  
  
RUN mv target/orienteer-examples.war /orienteer/  
RUN cp orienteer.properties /orienteer/  
RUN mvn clean  
RUN rm -rf orienteer-examples/  
  
WORKDIR /orienteer/  
RUN ln -s -f orienteer-examples.war active.war  

