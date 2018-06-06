FROM node:alpine  
  
MAINTAINER ukabuer <ukabuer@live.com>  
  
COPY . /dollars/  
WORKDIR /dollars  
RUN npm install && npm run build  
  
EXPOSE 3000  
CMD ["npm", "start"]

