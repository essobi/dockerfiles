FROM ubuntu:14.04  
MAINTAINER AFMensah, LLC  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get install -y wget  
RUN apt-get install -y -q openjdk-7-jre-headless  
RUN curl -k -L -o amp-realtime-data-1.2.7.zip
-unimbleus:8540ad9b559fb5ae28775a4c0831751c0ef004bf
'https://dl.bintray.com/nimbleus/afmensah/amp-realtime-data-1.2.7.zip'  
RUN mkdir /app  
RUN mv amp-realtime-data-1.2.7.zip /app  
WORKDIR /app  
RUN unzip amp-realtime-data-1.2.7.zip  
WORKDIR /app/amp-realtime-data-1.2.7/bin  
RUN chmod +x /app/amp-realtime-data-1.2.7/bin/amp-realtime-data  
EXPOSE 9000  
ENTRYPOINT ["/app/amp-realtime-data-1.2.7/bin/amp-realtime-data"]  

