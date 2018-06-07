FROM node:8.7  
MAINTAINER salim@hermidas.ch  
  
ENV appdir /usr/src/app/  
RUN mkdir -p $appdir  
WORKDIR $appdir  
  
# Install dependencies for accessing USB Bluetooth Dongle  
# Combine RUN apt-get update with apt-get install in the same RUN statement to
avoid caching issues (https://docs.docker.com/engine/userguide/eng-
image/dockerfile_best-practices/)  
RUN apt-get update && apt-get install -y bluez libusb-1.0-0-dev libudev-dev
usbutils  
RUN apt-get clean  
  
# Copy project files, install and rebuild node modules  
COPY . .  
  
RUN npm install  
RUN npm rebuild  
RUN chmod +x /usr/src/app/startup.sh  
  
EXPOSE 8080  
# Execute start script  
ENTRYPOINT ["/usr/src/app/startup.sh"]  

