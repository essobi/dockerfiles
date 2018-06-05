# Pull base image.  
FROM ubuntu:16.04  
  
# Install environment  
RUN apt-get -qq update && \  
apt-get install -y apt-utils && \  
apt-get install -y mc && \  
apt-get install -y sudo && \  
apt-get install -y git && \  
apt-get install -y nginx && \  
apt-get install -y curl && \  
apt-get install -y gnupg && \  
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - && \  
apt-get install -y build-essential && \  
apt-get install -y nodejs && \  
npm install -g npm@lts  
  
#Install project  
RUN mkdir -p /projects && \  
cd /projects && \  
git clone -b dev https://github.com/kpi-ua/ecampus.kpi.ua.git && \  
cd /projects/ecampus.kpi.ua && \  
npm install && \  
npm install -g grunt-cli && \  
npm install -g bower && \  
mkdir bower_components && \  
bower install --allow-root && \  
grunt build --force && \  
rm -rf /var/www/html && \  
ln -s /projects/ecampus.kpi.ua/app /var/www/html && \  
ln -s /projects/ecampus.kpi.ua/bower_components
/projects/ecampus.kpi.ua/app/bower_components  
  
#Generate self-signed certificate for nginx  
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout
/etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt
-subj "/C=UA/ST=Ukraine/L=Kiev/O=KPI/OU=KBIS/CN=campus.dev.kbis.kpi.ua" && \  
openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048  
  
#Generate nginx config file  
RUN echo 'server {\n\  
listen 80 default_server;\n\  
listen [::]:80 default_server;\n\  
listen 443 ssl default_server;\n\  
listen [::]:443 ssl default_server;\n\  
\n\  
root /var/www/html;\n\  
\n\  
server_name _;\n\  
\n\  
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;\n\  
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;\n\  
\n\  
location / {\n\  
try_files $uri $uri/ =404;\n\  
add_header Access-Control-Allow-Origin *;\n\  
add_header Access-Control-Allow-Credentials true;\n\  
}\n\  
}' > /etc/nginx/sites-available/default  
  
EXPOSE 80  
EXPOSE 443  
  
# Define default command.  
CMD ["nginx", "-g", "daemon off;"]  

