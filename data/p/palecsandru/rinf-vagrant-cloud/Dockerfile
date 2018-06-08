FROM ubuntu:16.04  
  
###############################################################################  
# System update  
###############################################################################  
RUN apt-get update  
RUN apt-get install -y wget  
  
###############################################################################  
# Vagrancy installation  
###############################################################################  
RUN mkdir -p /data  
RUN wget -q
https://github.com/ryandoyle/vagrancy/releases/download/0.0.4/vagrancy-0.0.4-linux-x86_64.tar.gz
-O /vagrancy.tar.gz  
RUN tar xf /vagrancy.tar.gz --strip 1  
  
EXPOSE 8099  
VOLUME ["/data"]  
  
###############################################################################  
# Start service  
###############################################################################  
CMD /vagrancy  

