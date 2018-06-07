FROM dogstudio/php:5.6-apache  
MAINTAINER Dogstudio <developers@dogstudio.be>  
  
RUN apt-get update && apt-get install -y ssmtp --no-install-recommends && rm
-r /var/lib/apt/lists/*  
RUN echo -e "\  
sendmail_path = /usr/sbin/ssmtp -t\n\  
mail.add_x_header = On\n\  
" >> /usr/local/etc/php/php.ini  
  
RUN echo -e "\  
mailhub=mailcatcher:1025\n\  
UseTLS=NO\n\  
FromLineOverride=YES\n\  
" > /etc/ssmtp/ssmtp.conf  

