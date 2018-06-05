FROM bezrukovp/main-base  
MAINTAINER Pavel Bezrukov "bezrukov.ps@gmail.com"  
# Install db server  
RUN apt-get -y -q install mysql-server-5.6 mysql-server-core-5.6 mysql-
common-5.6 mysql-client-5.6  
  
ADD etc/mysql/conf.d /etc/mysql/conf.d  
  
EXPOSE 3306  

