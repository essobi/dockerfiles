FROM factual/docker-base  
MAINTAINER Maxime DEVALLAND <maxime@factual.com>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5EDB1B62EC4926EA  
RUN echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-
updates/kilo main" > /etc/apt/sources.list.d/cloudarchive-kilo.list  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
--force-yes wget curl ntp pwgen ubuntu-cloud-keyring mariadb-server python-
mysqldb && rm -r /var/lib/apt/lists/*  
  
RUN sed -i -r 's/bind-address.*$/bind-address = 0.0.0.0/' /etc/mysql/my.cnf  
RUN rm -rf /var/lib/mysql  
  
RUN mkdir -p /etc/my_init.d/ /etc/service/mariadb  
ADD create_mariadb_admin_user.sh /create_mariadb_admin_user.sh  
ADD mariadb.sh /etc/service/mariadb/run  
  
EXPOSE 3306  

