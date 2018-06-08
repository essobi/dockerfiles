FROM nginx:stable-alpine  
  
RUN ln -snf /usr/share/zoneinfo/Europe/Rome /etc/localtime && \  
echo Europe/Rome > /etc/timezone && \  
rm -f /etc/nginx/nginx.conf && \  
rm -fr /etc/nginx/conf.d/  
  
COPY ./conf/nginx/nginx.conf /etc/nginx/  
COPY ./conf/nginx/proxyfcgi.conf /etc/nginx/conf.d/  
  
WORKDIR /var/www  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

