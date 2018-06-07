FROM openjdk:8  
MAINTAINER Nikola Petkanski <nikola@petkanski.com>  
  
RUN apt-get update \  
&& apt-get install -y wget git curl zip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/share/traccar  
  
WORKDIR /usr/share/traccar  
  
RUN wget -O traccar.zip
https://github.com/tananaev/traccar/releases/download/v3.6/traccar-
linux-64-3.6.zip  
  
RUN unzip traccar.zip  
  
RUN ./traccar.run  
  
EXPOSE 8082  
ENTRYPOINT /opt/traccar/bin/traccar start && tail -f
/opt/traccar/logs/tracker-server.log  
  

