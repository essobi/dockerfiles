FROM nginx:1.13.12-alpine  
  
MAINTAINER Tom Whitwell version: 1.0  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN chown -R nginx:nginx /usr/share/nginx  
  
EXPOSE 80  
STOPSIGNAL SIGTERM  
CMD ["nginx", "-g", "daemon off;"]  

