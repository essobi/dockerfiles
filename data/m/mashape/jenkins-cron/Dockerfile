FROM mcuadros/ofelia  
  
RUN apt-get update && apt-get install -qy python-pip groff-base  
RUN pip install awscli  
  
COPY config.ini /etc/ofelia/config.ini  

