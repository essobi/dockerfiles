FROM beevelop/nodejs-python:latest  
  
# Install app dependencies  
COPY package.json /src/package.json  
  
RUN cd /src; npm install  
  
# Bundle app source  
COPY . /src  
  
RUN node /src/server.js initfys  
EXPOSE 11111  
CMD ["node", "/src/server.js"]  

