FROM bankrate/jenkins-build-laravel:latest  
MAINTAINER Ryan Boyce  
  
RUN yum -y update && \  
yum -y remove php* nodesource-release remi-release && \  
yum -y --enablerepo=epel install mysql php71-bcmath php71-cli php71-common
php71-devel php71-intl php71-json php71-mcrypt php71-mysqlnd php71-pdo
php71-xml php71-xmlrpc php71-mbstring  

