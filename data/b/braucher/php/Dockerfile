# lamp stack built with puppet  
FROM braucher/puppet  
MAINTAINER Jeff Braucher <jeff@braucher.net>  
  
# Configure the system with puppet  
COPY ./puppet/ /puppet/  
ENV PUPPET_HOME /puppet  
RUN /puppet-apply  
  
# Install mysql-client  
RUN apt-get install -y mysql-client  
  
# Fix error_log parameter in php5-fpm.conf because puppet-php won't do it  
# (see php::fpm::config::error_log in php/puppet/php.yaml)  
RUN sed -i 's:^error_log.*:error_log = /proc/self/fd/2:' /etc/php5/fpm/php-
fpm.conf  
  
# Enable upload progress in apcu  
RUN echo apc.rfc1867 = 1 >> /etc/php5/mods-available/apcu.ini  
  
# Script to fix uids on host volumes  
COPY ./fix-uids /fix-uids  
  
# Run php  
EXPOSE 9000  
COPY ./app* /  
ENTRYPOINT ["/app"]  
CMD ["start"]  
  

