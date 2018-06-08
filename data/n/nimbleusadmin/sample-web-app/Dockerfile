FROM ubuntu:14.04  
MAINTAINER Nimbleus, LLC  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get install -y wget  
RUN apt-get install -y -q openjdk-7-jre-headless  
RUN curl -L -o sample-web-app-1.0.0-M6.2.zip
-unimbleus:8540ad9b559fb5ae28775a4c0831751c0ef004bf
'https://dl.bintray.com/nimbleus/nacreous/sample-web-app-1.0.0-M6.2.zip'  
RUN mkdir /app  
RUN mv sample-web-app-1.0.0-M6.2.zip /app  
WORKDIR /app  
RUN unzip sample-web-app-1.0.0-M6.2.zip  
WORKDIR /app/sample-web-app-1.0.0-M6.2/bin  
RUN chmod +x /app/sample-web-app-1.0.0-M6.2/bin/sample-web-app  
EXPOSE 9000  
ENTRYPOINT ["/app/sample-web-app-1.0.0-M6.2/bin/sample-web-app"]  

