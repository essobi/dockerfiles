FROM
node:6.10.0@sha256:af117acf2793c48aad74b70a78cb2e2cca28985f5dc57e73bb57f8b06548808c  
  
WORKDIR /usr/src/app  
  
COPY package.json ./package.json  
  
RUN npm install  
  
COPY ./ .  
  
RUN npm run bundle && npm ls substance  
  
EXPOSE 80  
ENTRYPOINT ["npm", "start"]  

