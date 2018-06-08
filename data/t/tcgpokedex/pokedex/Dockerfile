FROM node:5  
WORKDIR /app  
COPY ./package.json /app/package.json  
RUN npm install  
  
ENV NODE_ENV production  
ENV PORT 8000  
COPY . /app  
RUN npm run build  
  
WORKDIR /app/build  
  
EXPOSE 8000  
CMD npm start  
  

