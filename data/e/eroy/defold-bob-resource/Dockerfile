FROM node:alpine  
COPY resource /opt/resource  
RUN cd /opt/resource && \  
npm install --silent && \  
npm cache clean && \  
chmod 755 ./*  

