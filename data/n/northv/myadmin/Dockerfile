FROM maxexcloo/phpmyadmin  
  
ENV MYSQL_MAJOR=5.6  
ENV MYSQL_VERSION=5.6.25  
  
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
A4A9406876FCBD3C456770C88C718D3B5072E1F5  
RUN echo "deb http://repo.mysql.com/apt/debian/ wheezy mysql-${MYSQL_MAJOR}" >
/etc/apt/sources.list.d/mysql.list  
RUN apt-get update \  
&& apt-get install -y libmysqlclient18="${MYSQL_VERSION}"* \  
&& rm -rf /var/lib/apt/lists/*  
  

