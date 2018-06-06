FROM node:6.11.3  
# Create app directory  
RUN mkdir -p /usr/src/critical  
WORKDIR /usr/src/critical  
  
# Bundle app source  
COPY . /usr/src/critical  
  
# Install app dependencies  
RUN npm install -g gulp  
RUN npm install --save gulp  
RUN npm install -g critical  
RUN npm install --save critical  
  
CMD [ "node", "index.js" ]

