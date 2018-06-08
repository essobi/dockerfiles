# from template debian  
FROM renzok/umn-mapserver-cgi  
  
MAINTAINER Renzo Kottmann <renzo.kottmann@gmail.com>  
  
ENV APACHE_VERSION=2.4.10-10+deb8u4  
  
  
# Install the Apache Worker MPM (Multi-Procesing Modules)  
RUN apt-get -qq update --fix-missing \  
&& apt-get install -y \  
apache2=${APACHE_VERSION} \  
apache2-mpm-worker=${APACHE_VERSION}  
  
COPY vhost.conf /etc/apache2/sites-available/  
  
# Configure localhost in Apache  
RUN a2enmod actions cgi alias rewrite headers \  
&& sed -ri ' \  
s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \  
s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \  
s!^(\s*LogLevel)\s+\S+!\1 debug rewrite:trace3!g; \  
' /etc/apache2/apache2.conf \  
&& echo "ServerName justtosupresswarning" >> /etc/apache2/apache2.conf \  
&& echo "TransferLog /proc/self/fd/1" >> /etc/apache2/apache2.conf \  
&& a2ensite vhost  
#&& echo "LogLevel debug rewrite:trace3" >> /etc/apache2/apache2.conf  
#RUN chmod o+x /usr/local/bin/mapserv  
#RUN ln -s /usr/local/bin/mapserv /usr/lib/cgi-bin/mapserv  
# result in http://yourhostname.com/cgi-bin/mapserv # Volumes  
VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]  
# Expose ports  
EXPOSE 5555  
# Define default command  
CMD ["-D", "FOREGROUND"]  
  
ENTRYPOINT ["apache2ctl"]  
  

