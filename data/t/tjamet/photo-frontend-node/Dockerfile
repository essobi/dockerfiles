FROM node AS build  
  
RUN mkdir /src  
WORKDIR /src  
ADD package* /src/  
  
RUN npm install  
  
ADD . /src  
RUN npm run-script build  
  
FROM nginx:alpine  
COPY \--from=build /src/dist /usr/share/nginx/html  

