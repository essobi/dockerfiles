FROM buildpack-deps:xenial  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y apache2 build-essential apache2-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
curl -L https://github.com/wocommunity/wonder/archive/master.tar.gz | tar xz
&& \  
cd wonder-master/Utilities/Adaptors && \  
perl -pi -e 's/ADAPTOR_OS = MACOS/ADAPTOR_OS = LINUX/' make.config && \  
make ADAPTORS=Apache2.4 && \  
apxs2 -i -a -n WebObjects Apache2.4/mod_WebObjects.la && \  
cp Apache2.4/apache.conf /etc/apache2/apache_webobjects.conf  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN /usr/sbin/a2ensite default-ssl  
RUN /usr/sbin/a2enmod ssl  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

