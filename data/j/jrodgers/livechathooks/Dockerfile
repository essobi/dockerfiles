FROM node:slim  
  
EXPOSE 3000  
COPY app.js /  
COPY package.json /  
  
RUN npm install  
  
EXPOSE 3000  
CMD ["node", "app.js"]  

