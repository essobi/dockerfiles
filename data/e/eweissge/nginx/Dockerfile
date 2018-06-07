FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y \  
aptitude \  
htop \  
nginx \  
nmap \  
python-software-properties \  
screen \  
vim  
# Add files  
ADD webpage.tar.gz /var/www/html  
  
EXPOSE 80  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  
  

