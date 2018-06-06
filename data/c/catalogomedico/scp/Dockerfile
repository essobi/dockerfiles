FROM catalogomedico/nginx-php:latest  
MAINTAINER Sistemas CatMed <sistemas1@catalogomedico.com>  
  
# Configuracion de php.ini  
#----------------------------------------------------------  
#RUN apt-get install php5-apcu  
#----------------------------------------------------------  
# All enviroments  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php5/fpm/php.ini  
  
# Just poduction enviroment  
#RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/fpm/php.ini  
# Development enviroment  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/display_errors = .*/display_errors = On/" /etc/php5/fpm/php.ini  
RUN sed -i "s/; error_log = .*/error_log = \/var\/log\/error-php5.log/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/display_startup_errors = .*/display_startup_errors = On/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/; max_input_vars = .*/max_input_vars = 999999/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone.*/date.timezone = Europe\/Paris/"
/etc/php5/fpm/php.ini  
  
# Openssh  
RUN apt-get update  
RUN apt-get install -y openssh-server  
RUN mkdir -p ~/.ssh  
COPY docker/ssh/authorized_keys /root/.ssh/  
ADD docker/ssh/sshd_config /etc/ssh/sshd_config  
RUN chmod go-w ~/  
RUN chmod 700 ~/.ssh  
RUN chmod 600 ~/.ssh/authorized_keys  
RUN mkdir -p /var/run/sshd  
  
# Configuracion suvervisord  
ADD docker/supervisord.conf /etc/supervisor/conf.d/sshd.conf  
ADD docker/nginx/default.conf /etc/nginx/host.d/default.conf  
RUN mkdir -p /etc/nginx/ssl  
COPY docker/ssl/* /etc/nginx/ssl/  
  
# Configuracion codeigniter nginx: http://wiki.nginx.org/Codeigniter  
ADD docker/nginx-codeigniter/default-codeigniter.conf
/etc/nginx/addon.d/default-codeigniter.conf  
  
#max_children  
RUN sed -i "s/pm.max_children = 4/pm.max_children = 10/"
/etc/php5/fpm/pool.d/default.conf  
  
COPY . /data/http  
  
RUN chmod 777 /data/http/application/file_tmp  
  
EXPOSE 80  
EXPOSE 1011  
EXPOSE 443

