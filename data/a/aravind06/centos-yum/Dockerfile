FROM centos  
#Upgrade the current repo and system  
RUN yum update -y  
#Install base packages for the application  
#Disable interactive prompts during package installation  
RUN yum install -y git curl httpd php  
#Apply 10 seconds delay to complete the package installation  
RUN sleep 10  
#CMD ["yum", "install", "-y", "php-mcrypt php-mysql php-gd php-ldap"]  
#install necessary modules to work with the application  
RUN yum install -y php-mcrypt php-mysql php-gd  
RUN sleep 10  
#Install NFS package to mount EFS  
#RUN /sbin/service httpd start  
#RUN /sbin/chkconfig httpd on  
#RUN rm -rf /var/www/*  
#Create a directory to mount EFS  
#RUN mkdir /home/datastore  
#Mount EFS to /storage directory  
#RUN /bin/mount -t nfs4 $(curl -s http://169.254.169.254/latest/meta-
data/placement/availability-zone).fs-078a66ae.efs.us-west-2.amazonaws.com:/
/home/datastore  
#ENV ALLOW_OVERRIDE **False**  
#Change the document root to the desired location  
#RUN sed -i "s_/var/www/html/_/storage/var/www/html_" /etc/apache2/sites-
available/application.conf  
#Restart httpd  
#RUN service httpd start  
#Provide user and group permission for the document root  
#RUN /bin/chown -R www-data:www-data /storage/var/www/  
#Open the apache port 80  
EXPOSE 80  
CMD ["/sbin/service", "httpd", "start"]  
#Enable apache service to start evenafter reboot  
CMD ["/sbin/chkconfig", "httpd", "on"]  

