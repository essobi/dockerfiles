FROM node:8.4.0  
ENV HOST 0.0.0.0  
ENV PORT 10010  
WORKDIR /usr/src/app  
COPY ./package.json /usr/src/app/package.json  
RUN npm install  
  
COPY . /usr/src/app  
  
EXPOSE 10010  
CMD ["npm", "run", "start"]

