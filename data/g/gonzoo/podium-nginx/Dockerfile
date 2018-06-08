FROM debian:jessie  
  
MAINTAINER GonZOO <gonzoo@gonzoo.hu>  
  
RUN apt-get update && apt-get install -y \  
nginx \  
tcpflow \  
mc \  
nano  
  
ADD nginx.conf /etc/nginx/  
ADD site-available/dev.aspire.conf /etc/nginx/sites-enabled/dev.aspire.conf  
ADD site-available/uat.aspire.conf /etc/nginx/sites-enabled/uat.aspire.conf  
ADD site-available/prod.aspire.conf /etc/nginx/sites-enabled/prod.aspire.conf  
ADD site-available/stg.aspire.conf /etc/nginx/sites-enabled/stg.aspire.conf  
  
#RUN ln -s /etc/nginx/sites-available/site.conf /etc/nginx/sites-
enabled/symfony  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN echo "upstream php-upstream { server api:9000; }" >
/etc/nginx/conf.d/upstream.conf  
  
RUN usermod -u 1000 www-data  
  
CMD ["nginx"]  
  
EXPOSE 80  
EXPOSE 443  

