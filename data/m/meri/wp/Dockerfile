FROM centos:centos6  
MAINTAINER Mika Eriksson  
ENV REFRESHED_AT 2014-09-25  
RUN yum -y update && yum clean all  
RUN yum -y install mysql-server httpd php php-mysql wget tar && yum clean all  
RUN wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -ivh epel-release*  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN yum -y --enablerepo=remi install phpMyAdmin && yum clean all  
  
# install wordpress and create our default config  
#RUN wget http://wordpress.org/latest.tar.gz  
#RUN (tar zxvf latest.tar.gz && rm latest.tar.gz)  
RUN wget https://downloads.wordpress.org/release/en_GB/wordpress-4.0.tar.gz  
RUN (tar zxvf wordpress-4.0.tar.gz && rm wordpress-4.0.tar.gz)  
RUN rmdir /var/www/html  
RUN mv wordpress /var/www/html  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
ADD wp-config.php /var/www/html/wp-config.php  
ADD dot_htaccess /var/www/html/.htaccess  
RUN (cd /var/www; chown apache:apache * -R)  
RUN (cd /usr/share; chown apache:apache phpMyAdmin -R)  
  
# some help for interactive work  
RUN echo "alias l='ls -l'" >.bashrc  
RUN echo "alias a='tail -f /var/log/httpd/access.log'" >>.bashrc  
RUN echo "alias e='tail -f /var/log/httpd/error.log'" >>.bashrc  
#ADD import_db.sh import_db.sh  
EXPOSE 80  
# add default WordPressdb setup script  
ADD create_new_database.sql create_new_database.sql  
ADD startme.sh startme.sh  
  
# start httpd and mysqld and test if db exists - if not create it  
CMD /startme.sh  
  

