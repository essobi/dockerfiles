FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Installa il compilatore per nginx, wget, php5  
#RUN apt-get install -y gcc libpcre3 libpcre3-dev libssl-dev build-essential
php5 php5-fpm  
RUN apt-get install -y libpcre3 libpcre3-dev libssl-dev build-essential php5
php5-fpm apache2 libapache2-mod-php5  
RUN apt-get install -y shibboleth-sp2-schemas libshibsp-dev libshibsp-doc
libapache2-mod-shib2 opensaml2-tools  
RUN apt-get install -y vim htop wget git  
  
# Coping preparing scripts  
COPY scripts /tmp/scripts  
RUN chmod 744 /tmp/scripts -R  
  
# Ricompila e installa NGINX con i moduli per shibboleth  
#RUN /tmp/scripts/nginx.sh  
# Create index.html  
#RUN echo 'Hello Docker from NGINX' > /usr/local/nginx/html/index.html  
#RUN echo 'Hello Docker from APACHE2' > /var/www/html/index.html  
# Configuring APACHE  
COPY conf/apache/creaverifiche.conf /etc/apache2/sites-available/  
RUN /tmp/scripts/apache.sh  
COPY conf/apache/apache.pem /etc/apache2/ssl/  
  
# Configuring SHIBBOLETH2  
CMD ["/bin/mv", "/etc/shibboleth/shibboleth2.xml",
"/etc/shibboleth/shibboleth2.bk"]  
COPY conf/shibboleth/shibboleth2.xml /etc/shibboleth/shibboleth2.xml  
  
# Restarting services  
CMD ["/etc/init.d/shibd", "restart"]  
CMD ["/etc/init.d/apache2", "restart"]  
  
EXPOSE 80 443  
#CMD ["/bin/bash"]  
#CMD ["nginx", "-g", "daemon off;"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

