FROM node  
  
RUN mkdir /web-ms  
WORKDIR /web-ms  
  
COPY package.json .  
  
RUN npm install  
  
ADD . /web-ms  
  
EXPOSE 3100  
CMD ["npm","start"]

