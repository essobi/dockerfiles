FROM openjdk:8  
MAINTAINER cm0x4d <cm0x4d@codemonkey.ch>  
  
RUN apt-get install git  
RUN git clone https://github.com/Electrical-Age/ElectricalAge.git  
RUN cd ElectricalAge && ./gradlew build getAssets  
RUN mkdir -p ElectricalAge/run && echo "eula=true" >
ElectricalAge/run/eula.txt  
  
ENTRYPOINT cd ElectricalAge && ./gradlew runServer

