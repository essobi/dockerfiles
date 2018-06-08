FROM rok4/rok4:fastcgi  
  
ADD default.template /etc/nginx/sites-available/default.template  
ADD startNginx.sh /rok4/startNginx.sh  
  
RUN chmod -R 777 /rok4/* && apt-get install -y nginx  
  
CMD /rok4/startNginx.sh

