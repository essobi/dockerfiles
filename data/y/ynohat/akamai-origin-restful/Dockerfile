FROM node:8  
EXPOSE 80  
ENV PORT=80  
COPY package.json /  
RUN npm install --silent  
COPY index.js /  
  
CMD ["npm", "run", "start"]  

