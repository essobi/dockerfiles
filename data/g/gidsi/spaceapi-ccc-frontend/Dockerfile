FROM node as builder  
WORKDIR /app  
COPY . .  
  
RUN npm install  
RUN npm run build  
  
FROM nginx:alpine  
COPY \--from=builder /app/build/ /usr/share/nginx/html/  
RUN mkdir -p /tmp/osm/cache  
COPY nginx.conf /etc/nginx/nginx.conf  

