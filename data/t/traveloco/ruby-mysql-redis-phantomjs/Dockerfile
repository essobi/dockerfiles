FROM ruby:2.2.2  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends fonts-takao mysql-server tcl && \  
apt-get clean  
  
RUN { \  
echo '[mysqld]'; \  
echo 'character-set-server=utf8'; \  
echo 'collation-server=utf8_general_ci'; \  
echo '[client]'; \  
echo 'default-character-set=utf8'; \  
} > /etc/mysql/conf.d/charset.cnf  
  
ENV REDIS_VERSION 3.2.4  
RUN cd /tmp && \  
wget http://download.redis.io/releases/redis-$REDIS_VERSION.tar.gz && \  
tar xfvz redis-$REDIS_VERSION.tar.gz && \  
cd redis-$REDIS_VERSION && \  
make && \  
make install && \  
cd ../ && \  
rm -f redis-$REDIS_VERSION.tar.gz && \  
rm -rf redis-$REDIS_VERSION  
  
ENV PHANTOMJS_VERSION 2.1.1  
RUN cd /tmp && \  
wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar jxvf phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
mv phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/local/bin && \  
rm -f phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \  
rm -rf phantomjs-$PHANTOMJS_VERSION-linux-x86_64  

