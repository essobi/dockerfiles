FROM node:10.1.0-alpine as builder  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN npm install  
RUN npm install typescript@2.7.2  
  
COPY . /usr/src/app  
  
RUN npm run-script build  
  
# base image  
FROM nginx:1.13.12-alpine  
  
# copy artifact build from the 'build environment'  
COPY \--from=builder /usr/src/app/dist /usr/share/nginx/html  
  
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf  
  
# expose port 80  
EXPOSE 80  
# run nginx  
CMD ["nginx", "-g", "daemon off;"]  

