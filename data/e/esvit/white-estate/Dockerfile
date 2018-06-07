FROM node:5.10  
RUN mkdir /src  
WORKDIR /src  
  
# Bundle app source  
COPY ./ /src  
RUN npm install  
RUN npm run build  
RUN npm run css  
  
EXPOSE 8081  
CMD npm start  

