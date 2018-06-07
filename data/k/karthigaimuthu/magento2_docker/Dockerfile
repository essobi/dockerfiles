FROM ubuntu:16.04  
MAINTAINER Ewall Team <ewallteam@gmail.com>  
  
# Setup environment  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update sources  
RUN apt-get update -y  
  
# install http  
RUN apt-get install -y apache2 vim nano bash-completion net-tools zip unzip
curl  
RUN apt-get install -y git  
RUN mkdir -p /var/lock/apache2 /var/run/apache2  
ADD 000-default.conf /etc/apache2/sites-available/  
RUN a2enmod rewrite  
  
# Install mysql client and server  
RUN apt-get -y install curl  
  
#sendmail  
RUN apt-get -y install sendmail  
ADD sendmail.sh /home/sendmail.sh  
  
#move magento files to html folder  
RUN rm -rf /var/www/html/*  
ADD demo /var/www/html/  
ADD ./selldesk.sql /var/www/html/sql/  
RUN find /var/www/html -type f -exec chmod 644 {} \;  
RUN find /var/www/html -type d -exec chmod 755 {} \;  
RUN find /var/www/html/var -type d -exec chmod 777 {} \;  
RUN find /var/www/html/pub/media -type d -exec chmod 777 {} \;  
RUN find /var/www/html/pub/static -type d -exec chmod 777 {} \;  
RUN chmod 777 /var/www/html/app/etc  
RUN chmod 644 /var/www/html/app/etc/*.xml  
RUN chmod u+x /var/www/html/bin/magento  
COPY env.php /var/www/html/app/etc/  
COPY setup.sh /var/www/html/  
COPY cache.sh /var/www/html/  
  
# install php  
RUN apt-get -y update  
RUN apt-get install -y php7.0 libapache2-mod-php7.0 php7.0-common php7.0-curl
php7.0-gd php7.0-intl php7.0-cli php7.0-mbstring php7.0-mcrypt php7.0-pdo
php7.0-mysql php7.0-xml php7.0-xsl php7.0-soap php7.0-zip php7.0-json
php7.0-iconv  
  
# install sshd  
RUN apt-get update && apt-get install -y openssh-server openssh-client passwd  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22 8080 443  
CMD ["/usr/sbin/sshd", "-D"]  
  
#install composer  
RUN apt-get update && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#run the magento cron  
RUN apt-get -y install rsyslog  
ADD crontab /etc/crontab  
ADD start-cron.sh /usr/bin/start-cron.sh  
RUN chmod +x /usr/bin/start-cron.sh  
RUN touch /var/log/cron.log  
  
#run mysql restart  
RUN apt-get update  
RUN apt-get -y install mysql-client mysql-server  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  

