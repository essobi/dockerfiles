FROM soapdog/apache-lua  
MAINTAINER Andre Alves Garzia <andre@amoralabs.com>  
  
RUN apt-get update && apt-get -y install mysql-client libmysqlclient-dev curl
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN luarocks install luasql-mysql MYSQL_INCDIR=/usr/include/mysql && luarocks
install sailor  
  

