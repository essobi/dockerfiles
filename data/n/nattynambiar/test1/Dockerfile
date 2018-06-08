FROM node:0.10  
# COPY . /src  
# RUN cd /src; npm install  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /src && cp -a /tmp/node_modules /src/  
  
WORKDIR /src  
ADD . /src  
  
EXPOSE 8080  
CMD ["node", "/src/index.js"]  

