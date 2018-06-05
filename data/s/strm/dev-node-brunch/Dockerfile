FROM node:7.7.4  
RUN npm install -g brunch  
  
RUN mkdir /src  
  
WORKDIR /src  
COPY package.json /src  
RUN npm install  
  
EXPOSE 3333  
CMD ["npm", "start"]  

