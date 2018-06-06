############################################################  
# Dockerfile to build Cruise Control Installed Containers  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:latest  
  
# File Author / Maintainer  
MAINTAINER Kaushal Kishore <kaushal.rahuljaiswal@gmail.com>  
  
# Update the repository  
RUN apt-get update  
  
# Download and Installing Open JDK  
RUN apt-get -y install openjdk-6-jre  
RUN apt-get -y install openjdk-6-jdk  
  
# Download and Installing php libraries  
RUN apt-get -y install php5 libapache2-mod-php5 php5-mysql php5-gd php-pear
php-apc php5-curl curl lynx-cur  
  
# Download and Installing supervisor  
RUN apt-get -y install supervisor  
  
# Download and Installing git and vim  
RUN apt-get -y install git vim  
  
# Download and Installing zip unzip  
RUN apt-get -y install zip unzip  
  
# Dowloading and Intalling CruiseControl  
ADD
http://kaz.dl.sourceforge.net/project/cruisecontrol/CruiseControl/2.8.4/cruisecontrol-
bin-2.8.4.zip /cruisecontrol-bin-2.8.4.zip  
RUN unzip /cruisecontrol-bin-2.8.4.zip -d /opt/  
RUN mv /opt/cruisecontrol-bin-2.8.4 /opt/cruisecontrol  
  
# Downloading and Installing phpUnderControl  
RUN git clone git://github.com/phpundercontrol/phpUnderControl.git  
RUN php phpUnderControl/bin/phpuc.php install /opt/cruisecontrol  
RUN ln -s /usr/bin/java /bin/java  
  
# Installing PHPUnderControl pear library  
RUN pear channel-discover pear.phpundercontrol.org  
RUN pear channel-discover components.ez.no  
RUN pear install phpuc/phpUnderControl  
  
# Installing PHPDocumentor pear library  
RUN pear channel-discover pear.phpdoc.org  
RUN pear install phpdoc/phpDocumentor  
  
# Installing PHPCodeSniffer pear library  
RUN pear install PHP_CodeSniffer  
  
# Installing PHPDepend pear library  
RUN pear channel-discover pear.phpunit.de  
RUN pear channel-discover pear.pdepend.org  
RUN pear install pdepend/PHP_Depend  
  
# Installing PHPCPD pear library  
RUN pear channel-discover pear.phpmd.org  
RUN pear channel-discover pear.symfony.com  
RUN pear channel-discover pear.netpirates.net  
RUN pear install --alldeps phpunit/phpcpd  
  
# Installing PHPMD pear library  
RUN pear install phpmd/PHP_PMD  
  
# Adding cruisecontrol service file  
ADD cruisecontrol /etc/init.d/cruisecontrol  
ADD run.sh /run.sh  
  
# Adding configuration file  
ADD supervisord-cruisecontrol.conf /etc/supervisor/conf.d/supervisord-
cruisecontrol.conf  
  
# Adding execute permission to sh files  
RUN chmod 755 /run.sh  
  
# Set the port  
EXPOSE 8080  
  
# Set the volume  
VOLUME /opt/cruisecontrol/projects  
  
# Execut the run.sh  
CMD ["/run.sh"]  
  

