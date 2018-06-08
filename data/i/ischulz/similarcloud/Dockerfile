FROM node:latest  
RUN mkdir -p /user/src/similar  
WORKDIR /user/src/similar  
COPY . /user/src/similar  
RUN npm install  
EXPOSE 3003  
CMD npm run docker

