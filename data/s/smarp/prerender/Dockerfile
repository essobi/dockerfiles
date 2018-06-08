FROM node:4  
ENV NPM_CONFIG_LOGLEVEL warn  
  
# Install app dependencies  
COPY package.json /src/package.json  
RUN cd /src; npm install --production  
  
# Bundle app source  
COPY index.js /src/index.js  
  
WORKDIR "/src"  
  
EXPOSE 3000  
CMD ["node", "index.js"]  

