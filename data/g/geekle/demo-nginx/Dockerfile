FROM geekle/centos  
# Nginx  
RUN yum install -y nginx  
#chmod 777 /var/run/unicorn/unicorn.sock  
ADD server.crt /server.crt  
ADD server.key /server.key  
ADD nginx.conf /nginx.conf  
CMD nginx -c /nginx.conf  

