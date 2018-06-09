FROM polinux/centos7:latest  
MAINTAINER Przemyslaw Ozgo <linux@ozgo.info>  
  
RUN yum clean all && \  
yum install -y --nogpgcheck tar wget mariadb java-1.7.0-openjdk mariadb-server
git  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
# Create new Mysql DB setup  
RUN mysql_install_db --user=mysql --ldata=/var/lib/mysql/  
  
ADD install /data/install/  
  
RUN cd /data/install &&\  
./mysql.sh && \  
./install.sh  
  
RUN mv /data/install/mysql-connector-java-5.1.31-bin.jar
/usr/local/Stash/atlassian-stash/WEB-INF/lib/mysql-connector-
java-5.1.31-bin.jar  
  
ADD supervisord.conf /etc/supervisord.d/stash .conf  
EXPOSE 7990

