FROM alpine:3.7  
RUN apk update && \  
apk add nginx \  
nodejs \  
nodejs-npm  
  
COPY ./default.conf /etc/nginx/conf.d/default.conf  
  
COPY ./app /app  
  
EXPOSE 80  
CMD ["nginx", "-g", "pid /run/nginx.pid; daemon off;"]  

