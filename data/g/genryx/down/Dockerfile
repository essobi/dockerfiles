FROM genryx/docker-dl-tools:latest  
MAINTAINER glg8505@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /dl  
  
ADD dlfile ./dlfile  
  
RUN /bin/bash ./dlfile ; \  
megacopy --no-progress -u glg8505@gmail.com -p Togtojononna1* --local /dl
--remote /Root/down  

