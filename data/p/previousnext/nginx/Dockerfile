# Basic nginx container.  
FROM previousnext/base:latest  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
##  
# Nginx.  
##  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
RUN apt-get -y install nginx  
  
# Do not die when we have too many vhosts.  
RUN sed -i 's/# server_names_hash_bucket_size 64/server_names_hash_bucket_size
2048/g' /etc/nginx/nginx.conf  
  
##  
# Supervisord.  
##  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
EXPOSE 22 80  
CMD ["/root/start.sh"]  

