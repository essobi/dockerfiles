FROM node:6  
MAINTAINER Will Park <korea651@gmail.com>  
  
RUN mkdir -p /app  
  
WORKDIR /app  
ADD . /app  
  
RUN npm install  
  
ENV NODE_ENV development  
  
EXPOSE 3015 80  
CMD ["npm", "start"]

