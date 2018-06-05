FROM php:7.0-cli  
EXPOSE 80  
WORKDIR /data  
CMD ["php","-S","$(/sbin/ip route|awk '/default/ { print $3
}'):80","server.php"]  

