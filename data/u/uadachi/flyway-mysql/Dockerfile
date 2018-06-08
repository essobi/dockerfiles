FROM java:8  
MAINTAINER Yuta Adachi <ada-u@ada-u.com>  
  
# Install Flyway  
ENV FLYWAY_VERSION 3.2.1  
RUN wget -P /opt https://bintray.com/artifact/download/business/maven/flyway-
commandline-${FLYWAY_VERSION}-linux-x64.tar.gz && \  
cd /opt && \  
tar -xvf flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz && \  
rm flyway-commandline-${FLYWAY_VERSION}-linux-x64.tar.gz  
ENV PATH $PATH:/opt/flyway-${FLYWAY_VERSION}  
RUN flyway 2>&1 | grep "Flyway ${FLYWAY_VERSION}"  
  
# Install MySQL client  
ENV MYSQL_MAJOR 5.6  
ENV MYSQL_VERSION 5.6.30-1debian8  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
A4A9406876FCBD3C456770C88C718D3B5072E1F5  
RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-${MYSQL_MAJOR}" >
/etc/apt/sources.list.d/mysql.list  
RUN apt-get update && apt-get install -y mysql-client="${MYSQL_VERSION}"

