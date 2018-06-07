FROM node:6-slim  
  
MAINTAINER Oliver Lorenz <mail@oliverlorenz.com>  
  
RUN apt-get update && \  
apt-get install -y git && \  
git clone https://github.com/wkallhof/Hazel.git && \  
cd Hazel && npm install --production && \  
apt-get remove --purge -y git && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
ENV IP 0.0.0.0  
EXPOSE 8000  
WORKDIR /Hazel  
COPY config.default.js /Hazel/example/config.default.js  
  
ENTRYPOINT ["node", "example/server.js"]  
CMD []  

