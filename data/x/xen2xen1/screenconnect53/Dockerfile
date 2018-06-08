FROM debian:jessie  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get -y install wget  
  
# Clean  
RUN rm -rf /var/lib/apt/lists/*  
  
# Prepare directories  
RUN mkdir /opt/screenconnect-installer  
  
# Setup  
ADD
"https://d1kuyuqowve5id.cloudfront.net/ScreenConnect_5.5.10444.5898_Release.tar.gz"
/opt/screenconnect-installer/ScreenConnect_Release.tar.gz  
WORKDIR /opt/screenconnect-installer/  
  
# Volume  
VOLUME /opt/screenconnect/  
  
# Ports  
EXPOSE 8040 8041  

