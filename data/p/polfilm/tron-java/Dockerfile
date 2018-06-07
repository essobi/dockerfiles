FROM mlaccetti/docker-oracle-java8-ubuntu-16.04  
MAINTAINER polfilm  
  
# Install dependencies && Download java-tron  
RUN apt-get update  
RUN apt-get install git -y  
RUN git clone -b develop https://github.com/tronprotocol/java-tron.git
/home/java-tron  
  
# Change work directory  
WORKDIR /home/java-tron  
  
# RUN ./gradlew lint  
# RUN ./gradlew test  
# RUN ./gradlew build  
RUN ./gradlew clean shadowJar  
  

