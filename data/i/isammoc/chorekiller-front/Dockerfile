FROM node:6-alpine as builder  
COPY . /code  
WORKDIR /code  
RUN npm install -g @angular/cli  
RUN npm install -g yarn  
RUN npm cache --force clean  
RUN yarn install  
RUN ng build --prod  
  
FROM nginx:latest  
COPY \--from=builder /code/dist /app  
COPY ./docker/nginx/site.conf /etc/nginx/conf.d/default.conf  

