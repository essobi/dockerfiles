FROM debian  
MAINTAINER z0ne  
  
ADD ./start.sh /root  
RUN apt-get update &&\  
apt-get install -y php php-fpm nginx git &&\  
chmod +x /root/start.sh &&\  
git clone https://github.com/ripsscanner/rips.git /var/www/html/rips &&\  
rm -f /etc/nginx/sites-enabled/*  
  
ADD ./rips-nginx.conf /etc/nginx/sites-enabled/  
  
CMD [ "/root/start.sh" ]  
  
EXPOSE 80

