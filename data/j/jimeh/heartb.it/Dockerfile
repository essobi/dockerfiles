FROM node:5.11.1  
RUN mkdir /app  
WORKDIR /app  
COPY package.json /app/  
RUN npm install  
COPY . /app  
  
ENV PORT=80  
EXPOSE $PORT  
CMD ["npm", "start"]  

