From httpd:2.4  
MAINTAINER Yudai Kato <grandeur09@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y apache2-bin apache2-data  
RUN apt-get install -y libapache2-svn libapache-dbi-perl libapache2-mod-perl2
libdbd-mysql-perl libdigest-sha-perl libauthen-simple-ldap-perl  
RUN apt-get install -y curl ca-certificates  
  
ADD files/svn.conf /usr/local/apache2/conf/extra/svn.conf  
ADD files/httpd.conf /usr/local/apache2/conf/httpd.conf  
  
ADD files/docker-entrypoint.sh /entrypoint.sh  
CMD ["/entrypoint.sh"]  
  

