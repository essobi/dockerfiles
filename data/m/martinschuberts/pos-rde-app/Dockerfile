FROM node:8  
RUN mkdir -p /app  
WORKDIR /app  
  
ADD package.json /app  
RUN npm install  
  
COPY . /app  
RUN npm run build --prod  
  
FROM nginx  
  
#statically copy all code  
COPY \--from=0 /app/dist /usr/share/nginx/html/  
  
#TODO: could add a reverse proxy config here for rde-server calls

