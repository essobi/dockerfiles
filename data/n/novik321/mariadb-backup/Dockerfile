FROM mariadb:latest  
  
LABEL maintainer="novik321@gmail.com"  
  
VOLUME /home/nvzh/wordpress-site/var/lib/mysql  
  
RUN apt-get update && apt-get install -y \  
mariadb-backup-10.2 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 3306  
CMD ["mysqld"]  
  
  
# RUN echo "deb [arch=amd64,i386]
http://mirror.hosting90.cz/mariadb/repo/10.2/ubuntu xenial main\n\  
# deb-src http://mirror.hosting90.cz/mariadb/repo/10.2/ubuntu xenial main" >
/etc/apt/sources.list.d/MariaDB.list && \  
# apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8  

