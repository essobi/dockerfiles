FROM node:latest  
RUN mkdir /app  
WORKDIR /app  
COPY . /app  
COPY package.json package.json  
RUN npm install  
RUN npm run build  
EXPOSE 8000  
CMD ["npm", "start"]

