FROM debian:8  
MAINTAINER maxisoft  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
# curl is needed to download the xampp installer, net-tools provides netstat
command for xampp  
RUN apt-get -y install curl  
RUN apt-get -y install net-tools --no-install-recommends  
  
RUN curl -o xampp-linux-installer.run
"https://downloadsapachefriends.global.ssl.fastly.net/xampp-files/5.6.8/xampp-
linux-x64-5.6.8-0-installer.run?from_af=true" && \  
chmod +x xampp-linux-installer.run && \  
bash -c './xampp-linux-installer.run' && \  
ln -sf /opt/lampp/lampp /usr/bin/lampp && \  
rm xampp-linux-installer.run  
  
# Enable XAMPP web interface(remove security checks)  
RUN bash -c 'head --lines=-7 /opt/lampp/etc/extra/httpd-xampp.conf | tee
/opt/lampp/etc/extra/httpd-xampp.conf.new '  
RUN mv /opt/lampp/etc/extra/httpd-xampp.conf.new /opt/lampp/etc/extra/httpd-
xampp.conf  
  
# Create a /www folder and a symbolic link to it in /opt/lampp/htdocs. It'll
be accessible via http://localhost:[port]/www/  
# This is convenient because it doesn't interfere with xampp, phpmyadmin or
other tools in /opt/lampp/htdocs  
RUN mkdir /www  
RUN ln -s /www /opt/lampp/htdocs/  
  
# SSH server  
RUN apt-get install -y -q supervisor openssh-server --no-install-recommends  
RUN mkdir -p /var/run/sshd  
  
# Output supervisor config file to start openssh-server  
RUN echo "[program:openssh-server]" >> /etc/supervisor/conf.d/supervisord-
openssh-server.conf  
RUN echo "command=/usr/sbin/sshd -D" >> /etc/supervisor/conf.d/supervisord-
openssh-server.conf  
RUN echo "numprocs=1" >> /etc/supervisor/conf.d/supervisord-openssh-
server.conf  
RUN echo "autostart=true" >> /etc/supervisor/conf.d/supervisord-openssh-
server.conf  
RUN echo "autorestart=true" >> /etc/supervisor/conf.d/supervisord-openssh-
server.conf  
  
# Allow root login via password  
# root password is: root  
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
  
# Set root password  
# password hash generated using this command: openssl passwd -1 -salt xampp
root  
RUN sed -ri 's/root\:\\*/root\:\$1\$xampp\$5\/7SXMYAMmS68bAy94B5f\\./g'
/etc/shadow  
  
RUN apt-get clean  
VOLUME [ "/var/log/mysql/", "/var/log/apache2/" ]  
  
EXPOSE 3306  
EXPOSE 22  
EXPOSE 80  
RUN curl -o db.sql
https://raw.githubusercontent.com/maxisoft/m2test6/master/sql/db.sql  
RUN cp db.sql db_test.sql  
RUN sed -i -e "s/m2test6/m2test6-utest/g" db_test.sql  
  
RUN echo "/opt/lampp/lampp start \n\  
while ! /opt/lampp/bin/mysql -e 'use m2test6' >/dev/null 2>&1 \n\  
do \n\  
sleep 1 \n\  
/opt/lampp/bin/mysql < db.sql \n\  
/opt/lampp/bin/mysql < db_test.sql \n\  
done \n\  
/usr/bin/supervisord -n" > /startup.sh  
  
ENV MYSQL_DB_HOST localhost  
ENV MYSQL_DB_USERNAME root  
ENV MYSQL_DB_PASSWORD ""  
CMD ["sh", "/startup.sh"]  

