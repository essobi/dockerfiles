FROM node:6  
RUN mkdir /app  
COPY ./package.json /app  
WORKDIR /app  
  
RUN ["npm", "install"]  
  
COPY ./index.js /app  
  
EXPOSE 3000  
ENTRYPOINT ["node", "index.js"]  

