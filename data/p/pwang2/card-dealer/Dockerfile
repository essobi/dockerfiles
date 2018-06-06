FROM node:6.9.5-alpine  
COPY . /home/node/  
  
WORKDIR /home/node  
RUN npm install --silent  
  
ENV NODE_ENV production  
ENV PORT 80  
ENV MONGODB_URI=mongodb://localhost/card-dealer  
  
EXPOSE 80  
CMD ["npm", "start"]  

