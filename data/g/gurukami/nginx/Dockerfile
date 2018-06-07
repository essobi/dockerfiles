FROM nginx:1  
RUN rm /etc/nginx/conf.d/default.conf  
  
ADD etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD etc/nginx/conf.d/* /etc/nginx/conf.d/  
ADD etc/nginx/sites.d/* /etc/nginx/sites.d/  
ADD etc/nginx/ssl/default/* /etc/nginx/ssl/default/  
  
WORKDIR /share  
  
EXPOSE 80 443  

