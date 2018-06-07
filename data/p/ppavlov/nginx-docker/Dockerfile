FROM nginx:latest  
MAINTAINER Pavel Pavlov <ppavlov@nodomain>  
  
# config nginx  
RUN rm -rf /etc/nginx/conf.d/*  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD upstream.conf /etc/nginx/conf.d/upstream.conf  
ADD mime.types /etc/nginx/mime.types  
ADD sites-available/proxy-pass.conf /etc/nginx/sites-available/proxy-pass.conf  
RUN mkdir -p /etc/nginx/sites-enabled  
RUN ln -s /etc/nginx/sites-available/proxy-pass.conf /etc/nginx/sites-
enabled/proxy-pass.conf  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

