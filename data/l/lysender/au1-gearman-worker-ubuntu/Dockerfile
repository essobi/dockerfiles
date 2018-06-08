FROM lysender/ubuntu-php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN apt-get -y update && \  
apt-get -y install supervisor \  
libevent-2.0-5 \  
libgearman-dev \  
php5-gearman \  
php5-memcached \  
wget \  
openjdk-8-jre-headless \  
libmysql-java && apt-get clean  
  
# Install liquibase  
RUN mkdir /opt/liquibase  
RUN cd /opt/liquibase && wget
https://github.com/liquibase/liquibase/releases/download/liquibase-
parent-3.4.2/liquibase-3.4.2-bin.tar.gz  
RUN cd /opt/liquibase && tar xvzf liquibase-3.4.2-bin.tar.gz  
RUN ln -s /opt/liquibase/liquibase /usr/bin/liquibase  
  
# Configure blank services and let the mounted files do the work  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
RUN mkdir -p /etc/supervisor/conf.d  
  
VOLUME ["/data", "/var/log/supervisor"]  
CMD ["/bin/bash", "/start.sh"]  
  

