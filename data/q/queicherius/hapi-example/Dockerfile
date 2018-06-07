FROM node:6  
RUN mkdir -p /usr/api  
COPY . /usr/api  
WORKDIR /usr/api  
RUN npm install --production  
  
ENV PORT 3000  
EXPOSE $PORT  
  
CMD ["npm", "start"]

