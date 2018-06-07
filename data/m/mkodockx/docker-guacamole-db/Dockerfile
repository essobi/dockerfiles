FROM dockerfile/mariadb  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
# Define env vars  
ENV GUACAMOLE_VERSION 0.9.4  
ENV GUACAMOLE_AUTH_MYSQL_SHA1 a68166aec88784325f3358a16dedc70f2df73342  
  
ENV DB_PASS wh4zUP  
  
COPY create-user.sql /schema/000-create-user.sql  
  
# Fetch and install Guacamole MySQL auth extension.  
RUN mkdir -p /schema && \  
curl -L -o guacamole-auth-mysql.tar.gz
http://sourceforge.net/projects/guacamole/files/current/extensions/guacamole-
auth-mysql-0.9.4.tar.gz/download && \  
tar xzf guacamole-auth-mysql.tar.gz && \  
mv guacamole-auth-mysql-${GUACAMOLE_VERSION}/schema/*.sql /schema && \  
rm -rf guacamole-auth-mysql*  
  
#RUN touch /schema/000-create-user.sql && \  
# echo "CREATE USER 'guacamole'@'%' IDENTIFIED BY '${DB_PASS}';" >
/schema/000-create-user.sql && \  
# echo "GRANT SELECT,INSERT,UPDATE,DELETE ON guacamole.* TO 'guacamole'@'%';"
>> /schema/000-create-user.sql  
# Setup database when container is started  
RUN \  
echo "set -m" > /run.sh && \  
echo "mysqld_safe &" >> /run.sh && \  
echo "mysqladmin --silent --wait=30 ping || exit 1" >> /run.sh && \  
echo "mysqladmin create guacamole" >> /run.sh && \  
echo "cat /schema/*.sql | mysql guacamole" >> /run.sh && \  
echo "fg" >> /run.sh  
  
#RUN chmod -R a+rx /etc/mysql && \  
# chmod -R a+rwx /var/lib/mysql  
# conf and data volumes  
# VOLUME ["/etc/mysql", "/var/lib/mysql"]  
CMD ["bash", "/run.sh"]  

