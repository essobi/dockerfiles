#  
# MariaDB Dockerfile  
#  
# https://bitbucket.org/housesimple/docker-mariadb  
#  
FROM housesimple/centos  
  
MAINTAINER Olly Nevard <olly.nevard@housesimple.com>  
  
# Add MariaDB repo.  
ADD MariaDB.repo /etc/yum.repos.d/MariaDB.repo  
  
# Install MariaDB.  
RUN yum -y install MariaDB-server && \  
yum clean all  
  
# Define mountable directories.  
VOLUME ["/etc/my.cnf.d"]  
  
# Define entrypoint.  
ENTRYPOINT ["mysqld_safe"]  
  
# Expose ports.  
EXPOSE 3306  

