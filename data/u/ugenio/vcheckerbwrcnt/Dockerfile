FROM maven:3.3-jdk-7  
MAINTAINER Javier Cabezas Gívica y Eugenio F. González Martín  
  
#  
#Environment variable with repositories text file  
#  
ENV REPOSITORIES config.json  
  
#  
#Environment variable with java jar file  
#  
ENV JAVAJAR VCheckerBwr-0.0.1-SNAPSHOT.jar  
  
#  
# Copying the work directory into /usr/src/mymaven/  
#  
ADD $PWD /usr/src/mymaven/  
  
#  
# Placing us in this directory  
#  
WORKDIR /usr/src/mymaven  
  
#  
# Set up of required permissions on script file and VChecker file, installing
nodejs, npm and bower  
#  
RUN chmod 777 $JAVAJAR && apt-get update && apt-get -y install nodejs && apt-
get -y install npm && npm install -g bower  
  
#  
#running the VChecker when the container is run  
#  
ENTRYPOINT java -jar $JAVAJAR $REPOSITORIES  
  

