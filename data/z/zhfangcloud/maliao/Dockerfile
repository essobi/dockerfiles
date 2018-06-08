FROM alpine:latest  
  
MAINTAINER alex <alexwhen@gmail.com>  
  
RUN apk --update add nginx  
  
COPY FullScreenMario /usr/share/nginx/html  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

