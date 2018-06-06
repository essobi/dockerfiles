FROM centos/systemd  
# basic repo stuff: EPEL and Oracle MySQL GA  
RUN yum -y install epel-release  
RUN yum -y install --nogpgcheck https://dev.mysql.com/get/mysql57-community-
release-el7-11.noarch.rpm  
# Update  
#RUN yum -y distro-sync  
RUN yum -y install --nogpgcheck yum-utils \  
supervisor \  
hostname \  
iproute \  
perl-Data-Dumper \  
sysvinit-tools \  
dstat iproute tree vim openssh  
  
# Common for Enterprise and Community  
RUN yum -y install --nogpgcheck mysql-utilities  
  
# Community  
RUN yum -y install --nogpgcheck mysql-community-server \  
mysql-community-client mysql-router mysql-shell  
RUN yum -y install iproute  
  
# Remove all packages from image  
RUN yum -y clean all  
  
RUN rm /var/lib/mysql/* -fr  
RUN rm /var/lib/mysql-files/* -fr  
  
VOLUME /var/lib/mysql  
VOLUME /var/lib/mysql-files  
VOLUME /backup  
  
RUN useradd backup -d /backup -g mysql  
RUN chown -R mysql:mysql /var/lib/mysql  
RUN chown -R backup:mysql /backup  
  
COPY ./my.cnf /etc/  
COPY ./Dockerfile.systemd /Dockerfile.systemd  
  

