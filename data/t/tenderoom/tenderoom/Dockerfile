FROM nginx:1.10  
MAINTAINER sergey.bushnyak@sigrlami.eu  
  
# Add file for ELB healthcheker  
RUN mkdir -p /etc/nginx/html  
RUN touch /etc/nginx/html/elb-status  
  
RUN mkdir /etc/nginx/ssl  
COPY keys/ /etc/nginx/ssl/  
COPY ["./robots.txt", "./block.conf", "./nginx.conf", "./etc/nginx/"]  
  
# Needed when updating ssl keys  
#RUN mkdir -p /var/www/html  
#COPY tenderoom.com/ /var/www/html  
# Copy all configs to directory  
COPY conf/ /etc/nginx/conf.d/  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY docker-entrypoint.sh /opt/docker-entrypoint.sh  
  
RUN chmod a+x /opt/docker-entrypoint.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/opt/docker-entrypoint.sh"]  

