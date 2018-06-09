FROM node:latest  
COPY package.json package.json  
RUN npm install  
COPY . .  
EXPOSE 80 443 3030  
CMD ["npm","start"]

