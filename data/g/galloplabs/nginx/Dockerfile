FROM galloplabs/consul-template  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
RUN apk --update add nginx && rm -rf /var/cache/apk/*  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN chown -R nginx:nginx /var/lib/nginx  
  
EXPOSE 80  
EXPOSE 443  
CMD ["nginx"]  

