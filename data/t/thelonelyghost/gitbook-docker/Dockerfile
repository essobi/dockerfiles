FROM node:latest  
  
RUN apt-get update -yqqq  
RUN apt-get install -y apt-utils  
# Required with `--fix-missing' due to debian download servers being
unreliable  
RUN apt-get install -y calibre-bin || \  
apt-get install -y calibre-bin --fix-missing  
RUN npm install -g svgexport gitbook-cli  
RUN apt-get install -y libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev \  
build-essential g++  
RUN npm install -g canvas  
RUN rm -rf /var/lib/apt/lists/* /tmp/*  

