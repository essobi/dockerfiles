FROM alateam/ubuntu  
  
  
  
  
######### intall nginx an seting php  
RUN apt-get -y install nginx  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini  
ADD etc/vhost/default.conf /etc/nginx/sites-available/default  
  
RUN mkdir -p /workspace/logs/nginx  
  
#安装phpmyadmin  
RUN wget
http://jaist.dl.sourceforge.net/project/phpmyadmin/phpMyAdmin/4.3.9/phpMyAdmin-4.3.9-all-
languages.tar.gz -O - | tar -xz  
RUN mv phpMyAdmin* /phpmyadmin  
ADD etc/vhost/phpmyadmin.conf /etc/nginx/sites-available/phpmyadmin  
RUN ln -s /etc/nginx/sites-available/phpmyadmin /etc/nginx/sites-
enabled/phpmyadmin  
  
EXPOSE 22 80 81 82 3306 7474  
WORKDIR /runner  
ADD run.sh run.sh  
RUN chmod 755 *.sh  
CMD ["./run.sh"]  
# CMD ["/usr/sbin/sshd", "-D"]  

