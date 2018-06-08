FROM node:4.5.0  
ENV NPM_CONFIG_LOGLEVEL warn  
ENV NODE_ENV production  
  
WORKDIR /srv  
COPY package.json package.json  
RUN npm install  
COPY . .  
  
EXPOSE 9101  
CMD ["npm", "start", "-s"]  

