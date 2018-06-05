FROM uqlibrary/docker-base:13  
RUN rpm -ivh https://dev.mysql.com/get/mysql57-community-release-
el7-11.noarch.rpm  
  
COPY mysql-community.repo /etc/yum.repos.d/mysql-community.repo  
COPY mysqldump-to-s3.sh /root/mysqldump-to-s3.sh  
  
RUN \  
yum update -y && \  
yum install -y \  
mysql-community-client \  
mysql-community-common \  
mysql-community-libs && \  
chmod a+x /root/mysqldump-to-s3.sh && \  
mkdir /dumps  
  
ENTRYPOINT ["/root/mysqldump-to-s3.sh"]  

