FROM node:6.10.3  
MAINTAINER Michael Hsu <evenchange4@gmail.com>  
  
# Config  
ENV RELEASE_URL https://github.com/MCS-Lite/mcs-lite-
app/releases/download/v1.0.7/7688.tar.gz  
WORKDIR /app  
  
# Script  
RUN curl -L $RELEASE_URL | tar zx --strip-components 2  
RUN ls -lA  
  
# Expose  
EXPOSE 3000 8000  
ENTRYPOINT ["npm", "start"]  

