FROM node:latest  
COPY package.json /src/package.json  
RUN cd /src; npm install  
COPY . /src  
EXPOSE 22222  
CMD ["node", "/src/server.js"]  

