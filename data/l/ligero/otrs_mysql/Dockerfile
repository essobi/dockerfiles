FROM ubuntu:16.04  
MAINTAINER Complemento <https://www.complemento.net.br>  
  
# Install database  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y supervisor \  
apt-utils \  
mysql-server \  
libterm-readline-perl-perl \  
locales && \  
locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
COPY z_my_otrs.cnf /etc/mysql/mysql.conf.d/  
  
# Supervisor  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
COPY mysql.sh /opt/src/  
RUN chmod 755 /opt/src/mysql.sh  
  
# See Bug https://stackoverflow.com/questions/9083408/fatal-error-cant-open-
and-lock-privilege-tables-table-mysql-host-doesnt-ex  
RUN chown -R mysql:mysql /var/lib/mysql  
  
EXPOSE 3306  
CMD ["/opt/src/mysql.sh"]  

