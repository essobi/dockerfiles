FROM node  
  
RUN mkdir -p /app  
WORKDIR /app  
COPY package.json /app/  
COPY . /app  
  
RUN npm install  
  
RUN cd /app  
  
EXPOSE 3000  
CMD npm start

