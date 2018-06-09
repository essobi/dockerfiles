FROM ubuntu:trusty  
MAINTAINER Filipe Oliveira "contato@fmoliveira.com.br"  
# Update APT repositories  
RUN apt-get update  
  
# Setup Git and clone the repository  
RUN apt-get install -y git && \  
git clone https://github.com/nied-unicamp/TelEduc.git /var/www  
  
# Setup MySQL  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y mysql-server && \  
service mysql start && \  
mysqladmin -u root password Teleduc123!  
  
# Setup Nginx + PHP5  
RUN apt-get install -y nginx php5-fpm php5-mysql && \  
service php5-fpm start  
  
ADD nginx-site.conf /etc/nginx/sites-available/default  
  
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini
&& \  
service php5-fpm restart  
  
# Start the web server  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

