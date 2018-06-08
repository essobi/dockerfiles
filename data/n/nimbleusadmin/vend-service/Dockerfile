FROM ubuntu:14.04  
MAINTAINER Nimbleus, LLC  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get install -y wget  
RUN apt-get install -y -q openjdk-7-jre-headless  
RUN curl -k -L -o vend-service-0.2.3.zip
-unimbleus:8540ad9b559fb5ae28775a4c0831751c0ef004bf
'https://dl.bintray.com/nimbleus/libertyvending/vend-service-0.2.3.zip'  
RUN mkdir /app  
RUN mv vend-service-0.2.3.zip /app  
WORKDIR /app  
RUN unzip vend-service-0.2.3.zip  
WORKDIR /app/vend-service-0.2.3/bin  
RUN chmod +x /app/vend-service-0.2.3/bin/vend-service  
EXPOSE 9000  
ENTRYPOINT ["/app/vend-service-0.2.3/bin/vend-service"]  

