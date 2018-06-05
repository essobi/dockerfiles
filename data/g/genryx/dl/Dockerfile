FROM genryx/docker-dl-tools:latest  
MAINTAINER glg8505@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /dl  
  
ADD dlfile ./dlfile  
  
RUN /bin/bash ./dlfile ; \  
megacopy --no-progress -u anestodta@gmail.com -p "T0r0buSy" \--local /dl
--remote /Root/dl  

