FROM debian  
  
# Set up LLMP server  
RUN apt-get update && apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y lighttpd php5-cgi
php5-mysql unzip mysql-server mysql-client  
RUN lighttpd-enable-mod fastcgi  
RUN lighttpd-enable-mod fastcgi-php  
RUN rm /var/www/html/index.lighttpd.html  
  
# Install LWT  
#COPY lwt_v_1_6_1.zip /tmp/lwt.zip  
ADD http://downloads.sourceforge.net/project/lwt/lwt_v_1_6_1.zip /tmp/lwt.zip  
RUN cd /var/www/html && unzip /tmp/lwt.zip && rm /tmp/lwt.zip  
RUN mv /var/www/html/connect_xampp.inc.php /var/www/html/connect.inc.php  
RUN chmod -R 755 /var/www/html  
  
EXPOSE 80  
CMD /etc/init.d/mysql start && /etc/init.d/lighttpd start && sleep infinity  
  
# docker built -t lwt .  
# docker run -it -p 8010:80 lwt  

