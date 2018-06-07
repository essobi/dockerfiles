FROM node:0.10  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ENV NODE_ENV production  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
  
EXPOSE 3000  
ENV REDIS_URL redis://redis  
  
CMD [ "npm", "start" ]

