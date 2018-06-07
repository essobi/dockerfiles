FROM node:8.9.4  
RUN mkdir /app  
ADD package.json /app  
WORKDIR /app  
RUN npm install  
WORKDIR ..  
ADD . /app  
WORKDIR /app  
RUN ls  
EXPOSE 3005  
CMD npm run docker

