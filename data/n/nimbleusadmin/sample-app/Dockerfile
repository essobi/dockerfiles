FROM ubuntu:14.04  
MAINTAINER Nimbleus, LLC  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get install -y wget  
RUN apt-get install -y -q openjdk-7-jre-headless  
RUN curl -k -L -o sample-app-1.0.0-RC8.zip
-unimbleus:8540ad9b559fb5ae28775a4c0831751c0ef004bf
'https://dl.bintray.com/nimbleus/nacreous/sample-app-1.0.0-RC8.zip'  
RUN mkdir /app  
RUN mv sample-app-1.0.0-RC8.zip /app  
WORKDIR /app  
RUN unzip sample-app-1.0.0-RC8.zip  
WORKDIR /app/sample-app-1.0.0-RC8/bin  
RUN chmod +x /app/sample-app-1.0.0-RC8/bin/sample-app  
EXPOSE 9000  
ENTRYPOINT ["/app/sample-app-1.0.0-RC8/bin/sample-app"]  

