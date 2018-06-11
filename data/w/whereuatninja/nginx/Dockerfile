FROM nginx:latest  
  
MAINTAINER info@whereuat.ninja  
  
VOLUME /var/cache/nginx  
  
# Copy custom nginx config  
COPY docker/config/nginx.development.conf /etc/nginx/nginx.conf  
  
# Copy custom nginx config  
COPY public /var/www/public  
  
EXPOSE 80 443  
ENTRYPOINT ["nginx"]  
CMD ["-g", "daemon off;"]  
  
# To build:  
# docker build -f docker/docker-nginx.dockerfile --tag whereuatninja/nginx .  
# To run:  
# docker run -d -p 80:6379 --name nginx whereuatninja/nginx

