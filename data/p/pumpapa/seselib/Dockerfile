FROM beevelop/nodejs-python:latest  
  
# Install app dependencies  
COPY package.json /src/package.json  
  
RUN cd /src; npm install  
  
# Bundle app source  
COPY . /src  
  
EXPOSE 22222  
CMD ["node", "/src/server.js"]  

