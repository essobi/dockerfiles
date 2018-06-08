FROM phusion/baseimage  
  
EXPOSE 80  
# APT dependencies  
RUN apt-get update && \  
apt-get -y install git \  
php5 apache2 libapache2-mod-php5 php5-mysql php5-cli mysql-client \  
mysql-server && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# MySQL service  
RUN mkdir /etc/service/mysql && \  
echo "#!/bin/bash" > /etc/service/mysql/run && \  
echo "mysqld_safe" >> /etc/service/mysql/run && \  
chmod +x /etc/service/mysql/run  
  
# Apache service  
RUN mkdir /etc/service/apache2 && \  
echo "#!/bin/bash" > /etc/service/apache2/run && \  
echo "exec apache2ctl -DNO_DETACH" >> /etc/service/apache2/run && \  
chmod +x /etc/service/apache2/run  
  
# Install Q2A  
RUN rm -rf /var/www/html && \  
git clone https://github.com/q2a/question2answer.git /var/www/html && \  
mv /var/www/html/qa-config-example.php /var/www/html/qa-config.php  
  
# Configure Q2A  
RUN sed -i -e 's/your-mysql-username/root/' /var/www/html/qa-config.php && \  
sed -i -e 's/your-mysql-password//' /var/www/html/qa-config.php && \  
sed -i -e 's/your-mysql-db-name/q2a/' /var/www/html/qa-config.php  
  
ADD setup-project.sh /etc/my_init.d/setup-project.sh  

