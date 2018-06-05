From alpine:3.3  
RUN apk add --update g++ git krb5-dev make nodejs openssh python && rm -rf
/var/cache/apk/*  
RUN npm install -g git://github.com/mvertes/gcr.git  
  
CMD ["gcr"]  

