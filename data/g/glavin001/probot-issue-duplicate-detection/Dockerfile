FROM glavin001/alpine-python2-numpy-scipy:latest  
MAINTAINER Glavin Wiechert <glavin.wiechert@gmail.com>  
  
# Defines our working directory in container  
WORKDIR /usr/src/app  
  
# Copy the application project  
COPY package.json ./  
RUN npm install  
  
# Build  
COPY src/ src/  
  
# Enable systemd init system in container  
# ENV INITSYSTEM on  
# Run on device  
EXPOSE 3000  
CMD npm run start  

