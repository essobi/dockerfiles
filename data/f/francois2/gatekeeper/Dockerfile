FROM kkarczmarczyk/node-yarn:6.9  
WORKDIR /gatekeeper  
  
COPY package.json /gatekeeper/  
RUN yarn install  
COPY . /gatekeeper/  
  
USER nobody  
CMD node server.js  

