  
FROM debian:jessie  
LABEL maintainer='cory(at)secureideas(dot)com'  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update --fix-missing  
  
# curl is needed to download the xampp installer, net-tools provides netstat
command for xampp  
RUN apt-get -y install curl net-tools  
  
RUN curl -o xampp-linux-installer.run
"https://downloadsapachefriends.global.ssl.fastly.net/xampp-
files/5.6.21/xampp-linux-x64-5.6.21-0-installer.run?from_af=true"  
RUN chmod +x xampp-linux-installer.run  
RUN bash -c './xampp-linux-installer.run'  
RUN ln -sf /opt/lampp/lampp /usr/bin/lampp  
  
# Enable XAMPP web interface(remove security checks)  
RUN sed -i.bak s'/Require local/Require all granted/g'
/opt/lampp/etc/extra/httpd-xampp.conf  
  
# Enable includes of several configuration files  
RUN mkdir /opt/lampp/apache2/conf.d && \  
echo "IncludeOptional /opt/lampp/apache2/conf.d/*.conf" >>
/opt/lampp/etc/httpd.conf  
  
# SSH server  
RUN apt-get install -y -q supervisor openssh-server  
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
  
# Few handy utilities which are nice to have  
RUN apt-get -y install nano vim less git --no-install-recommends  
  
RUN apt-get clean  
VOLUME [ "/var/log/mysql/", "/var/log/apache2/" ]  
  
EXPOSE 3306  
EXPOSE 22  
EXPOSE 80  
# write a startup script  
RUN echo '/opt/lampp/lampp start' >> /startup.sh  
RUN echo '/usr/bin/supervisord -n' >> /startup.sh  
  
# MUTILLIDAE SETUP ====  
# clone current upstream mutillidae  
RUN git clone git://git.code.sf.net/p/mutillidae/git mutillidae-git  
# put the mutillidae src into www  
RUN rm -rf /opt/lampp/htdocs/*  
RUN rm -rf mutillidae-git/.settings/  
RUN cp -r mutillidae-git/. /opt/lampp/htdocs/  
# TEMP: fix the include in MySQLHandler.php  
RUN sed -ri 's/includes\/database-
config.php/\/opt\/lampp\/htdocs\/includes\/database-config.php/g'
/opt/lampp/htdocs/classes/MySQLHandler.php  
# change the htaccess to allow the host VM to access, this has to be done
since mutillidae is running in a docker container.  
RUN sed -ri 's/Deny from all/Allow from all/g' /opt/lampp/htdocs/.htaccess  
#ADD mutillidae_imgs ./mutillidae_imgs  
#RUN cp mutillidae_imgs/coykillericon-50-38.png /opt/lampp/htdocs/images/  
# replace background colors  
#RUN cd /opt/lampp/htdocs/ && find . -name '*.php' -type f -exec sed -ri
's/#ccccff/2d2d2d/g' {} \;  
# Add the new css global styles file  
#COPY mutillidae.css /opt/lampp/htdocs/styles/global-styles.css  
# clean up  
RUN rm -rf mutillidae-git/  
  
CMD ["sh", "/startup.sh"]  
  
# docker run -it -e DOCKER_HOST=$(/sbin/ip route|awk '/default/ { print $3 }')  

