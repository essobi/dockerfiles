FROM java:8-jre  
MAINTAINER Phil Plante <phil@rentlytics.com>  
  
WORKDIR /usr/local/sauce-connect  
  
RUN apt-get install -qq wget unzip  
RUN wget http://saucelabs.com/downloads/Sauce-Connect-latest.zip && unzip
Sauce-Connect-latest.zip  
  
ENTRYPOINT ["java", "-jar", "Sauce-Connect.jar"]  

