FROM ubuntu:14.04  
  
MAINTAINER Wilhelm Stephan, Leon Graser, Dominik Bäßler  
  
# Install Java 8  
# ---------------  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install -y python-software-properties && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
  
# Folders  
# -------  
RUN mkdir -p /srv/salt/fapra/configs && \  
mkdir -p /srv/salt/fapra/formulas/backup && \  
mkdir -p /srv/salt/fapra/formulas/connect && \  
mkdir -p /srv/salt/fapra/formulas/mysql && \  
mkdir -p /srv/salt/fapra/formulas/restore && \  
mkdir -p /srv/salt/fapra/formulas/wordpress && \  
mkdir -p /srv/salt/fapra/tmp && \  
mkdir -p /fapra && \  
mkdir -p /api  
  
# Files  
# ----------------------------  
# configs  
COPY configs/my.cnf /srv/salt/fapra/configs/my.cnf  
COPY configs/wp-config.php /srv/salt/fapra/configs/wp-config.php  
# formulas -> backup  
COPY formulas/backup/backup_amazon.sls
/srv/salt/fapra/formulas/backup/backup_amazon.sls  
COPY formulas/backup/backup_ubuntu.sls
/srv/salt/fapra/formulas/backup/backup_ubuntu.sls  
COPY formulas/backup/init.sls /srv/salt/fapra/formulas/backup/init.sls  
# formulas -> connect  
COPY formulas/connect/connect_amazon.sls
/srv/salt/fapra/formulas/connect/connect_amazon.sls  
COPY formulas/connect/connect_ubuntu.sls
/srv/salt/fapra/formulas/connect/connect_ubuntu.sls  
COPY formulas/connect/init.sls /srv/salt/fapra/formulas/connect/init.sls  
# formulas -> mysql  
COPY formulas/mysql/mysql_amazon.sls
/srv/salt/fapra/formulas/mysql/mysql_amazon.sls  
COPY formulas/mysql/mysql_ubuntu.sls
/srv/salt/fapra/formulas/mysql/mysql_ubuntu.sls  
COPY formulas/mysql/init.sls /srv/salt/fapra/formulas/mysql/init.sls  
# formulas -> restore  
COPY formulas/restore/restore_amazon.sls
/srv/salt/fapra/formulas/restore/restore_amazon.sls  
COPY formulas/restore/restore_ubuntu.sls
/srv/salt/fapra/formulas/restore/restore_ubuntu.sls  
COPY formulas/restore/init.sls /srv/salt/fapra/formulas/restore/init.sls  
# formulas -> wordpress  
COPY formulas/wordpress/wordpress_amazon.sls
/srv/salt/fapra/formulas/wordpress/wordpress_amazon.sls  
COPY formulas/wordpress/wordpress_ubuntu.sls
/srv/salt/fapra/formulas/wordpress/wordpress_ubuntu.sls  
COPY formulas/wordpress/init.sls /srv/salt/fapra/formulas/wordpress/init.sls  
# other  
COPY main.proto /api/main.proto  
COPY gRPCContainer.jar /fapra/gRPCContainer.jar  
  
# Install saltStack  
# -----------------  
RUN add-apt-repository ppa:saltstack/salt -y && \  
add-apt-repository ppa:saltstack/salt2015-5 -y && \  
apt-get update && \  
apt-get install -y salt-api && \  
apt-get install -y salt-cloud && \  
apt-get install -y salt-master && \  
apt-get install -y salt-minion && \  
apt-get install -y salt-ssh && \  
apt-get install -y salt-syndic && \  
apt-get clean  
  
VOLUME /api  
EXPOSE 40011  
CMD ["java", "-jar", "/fapra/gRPCContainer.jar", "40011"]  

