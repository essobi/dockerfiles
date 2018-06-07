FROM ubuntu  
  
RUN apt-get update  
RUN apt-get -y install unzip curl  
  
RUN mkdir /external-data-sources/  
RUN cd /external-data-sources/  
WORKDIR /external-data-sources/  
COPY get-city-path.sh /scripts/get-city-path.sh  
RUN . /scripts/get-city-path.sh  
VOLUME /external-data-sources/  

