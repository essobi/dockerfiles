# Pull base image.  
FROM teamrock/apache2:production  
  
#FROM tutum/lamp  
#  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server
php5-imagick php5-gd php5-intl php5-mcrypt php5-apcu php5-curl php5-mysql  
  
# Add our virtual-host.conf  
ADD ./virtual-host.conf /etc/apache2/sites-enabled/0-virtual-host.conf  
  
# Add our initialisation script  
ADD ./run.sh /tmp/run.sh  
  
# Add punditTransformer symfony app  
ADD ./punditTransformer /var/www/  
  
#Create Mysql admin user  
#RUN service mysql start; mysql -u root -e "CREATE USER 'admin'@'%' IDENTIFIED
BY 'pass';";mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO 'admin'@'%' WITH
GRANT OPTION;";  
# Commands we need in order to say BOOM  
ENTRYPOINT [ "/bin/bash", "/tmp/run.sh" ]  
  

