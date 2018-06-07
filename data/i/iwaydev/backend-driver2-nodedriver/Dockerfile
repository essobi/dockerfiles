FROM node:8.5  
EXPOSE 5001  
RUN mkdir -p /usr/src/apps/nodeDriver  
WORKDIR /usr/src/apps/nodeDriver  
COPY package.json /usr/src/apps/nodeDriver  
RUN npm install  
RUN npm install forever -g

