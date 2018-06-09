FROM nginx:alpine  
MAINTAINER Andreas Eiselt <andreas.eiselt@gmail.com>  
  
EXPOSE 80  
RUN apk update  
RUN apk add bash bash-completion s6  
RUN rm -rf /var/cache/apk/*  
  
WORKDIR /var/www  
CMD ["/bin/s6-svscan", "/etc/s6"]  
  
ADD rootfs /  

