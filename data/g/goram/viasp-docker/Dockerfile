FROM centos:6.8  
MAINTAINER Mateusz Gora  
# Install Required RPM Packages  
RUN yum install httpd -y; yum clean all  
RUN yum install mysql-server mysql -y; yum clean all  
RUN yum install php php-mysqli -y; yum clean all  
# Initialize Database Directory  
RUN chkconfig mysqld on  
RUN service mysqld start && sleep 10  
RUN chkconfig httpd on  
##################### INSTALLATION END #####################  
EXPOSE 80  
RUN echo 'TEST' > /var/www/html/index.html  
CMD ["/sbin/init"]  

