FROM nginx:alpine  
WORKDIR /app  
  
RUN apk --no-cache add --virtual nodejs nodejs-npm  
  
COPY package.json /app  
RUN npm install  
COPY . /app  
  
RUN npm run build  
  
RUN rm -rf /usr/share/nginx/html && mv /app/dist/ /usr/share/nginx/html/  
  
EXPOSE 80  

