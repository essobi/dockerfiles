FROM ubuntu:trusty  
  
MAINTAINER tony.hirst@gmail.com  
  
# Install Headless JRE after updating installed packages.  
RUN apt-get update && apt-get install -y unzip openjdk-7-jre-headless wget  
RUN apt-get clean  
  
RUN wget --no-check-certificate
https://github.com/tabulapdf/tabula/releases/download/v1.0.1/tabula-
jar-1.0.1.zip  
RUN unzip tabula-jar-1.0.1.zip -d /opt && rm tabula-jar-1.0.1.zip  
  
EXPOSE 8080  
CMD ["java","-Dfile.encoding=utf-8","-Xms256M","-Xmx1024M","-jar",
"/opt/tabula/tabula.jar"]  
  

