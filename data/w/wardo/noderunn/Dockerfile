FROM node:8.11.2  
WORKDIR /app  
ADD . /app  
RUN npm install  
EXPOSE 7200  
ENV NODE_ENV test  
CMD ['node', 'src/index.js']  

