FROM openjdk:8-jre-slim  
  
RUN mkdir -p /opt/JDownloader/  
RUN apt-get update -y && apt-get install -y megatools  
WORKDIR /opt/JDownloader  
RUN megadl
'http://mega.nz/#!mctCnIhC!fNqx1UOf06cVB7h9Cis1Kk5J_tAGMTFsSQcuQ2FPfYw'  
  
CMD java -jar /opt/JDownloader/JDownloader.jar  

