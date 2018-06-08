FROM alpine  
RUN apk update && apk upgrade && apk add --update nginx && rm -rf
/var/cache/apk/*  
  
CMD ["nginx", "-g", "pid /tmp/nginx.pid; daemon off;"]  

