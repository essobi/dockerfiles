FROM java:8  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /  
EXPOSE 5000  
ADD . /opt/  
WORKDIR /opt/  
RUN ["mvn", "clean"]  
RUN mvn package -X -Dmaven.test.skip=true  
RUN mv target/DensityMap-0.0.1-SNAPSHOT.jar target/density_maps.jar  
  
CMD java -jar target/density_maps.jar  
  

