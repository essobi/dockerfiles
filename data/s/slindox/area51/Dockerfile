FROM alpine:latest  
  
LABEL maintainer="Léon Mikeleit <lpmikeleit@gmail.com>"  
LABEL description="Example Dockerfile with NGINX"  
  
RUN apk add --update nginx && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /tmp/nginx/  
  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/default.conf /etc/nginx/conf.d/default.conf  
ADD files/html.tar.gz /usr/share/nginx/  
  
EXPOSE 80/tcp  
  
ENTRYPOINT ["nginx"]  
CMD ["-g", "daemon off;"]  
  

