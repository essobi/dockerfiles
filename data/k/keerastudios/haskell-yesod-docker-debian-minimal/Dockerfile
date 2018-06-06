# A minimal debian that can be used with Yesod.  
FROM bitnami/minideb:latest  
  
# Keera Studios  
MAINTAINER Ivan Perez (Keera Studios) version: 0.1  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y apt-utils && apt-get install -y
libgmp10 && apt-get clean && rm -rf /var/lib/apt/lists/*  

