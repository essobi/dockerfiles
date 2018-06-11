FROM ubuntu  
  
RUN apt-get update && apt-get install -y wget  
  
ENV version 1.4.5  
RUN mkdir -p /opt/upscuits && mkdir -p /var/www/status  
  
WORKDIR /opt/upscuits  
  
RUN wget https://github.com/digibart/upscuits/archive/v${version}.tar.gz -O -
| tar --strip-components=1 -xz  
  
RUN cp -r public/* /var/www/status/  
  
CMD sh  

