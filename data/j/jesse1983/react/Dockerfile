FROM node:6.4.0  
RUN npm i supervisor bower gulpjs/gulp#4.0 -g  
RUN mkdir /app/  
WORKDIR /app  
COPY . /app  
RUN npm install  
CMD ["npm","start"]

