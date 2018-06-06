# Self contained Redmine install (Ruby, Mysql, Passenger Standalone)  
# Centos 6.5, Ruby 2.0, Redmine 2.4  
# also includes Rsync for migrating from remote server  
#  
# VERSION 1  
# use blalor/centos bare bones centos 6.5 image  
FROM blalor/centos  
  
MAINTAINER webts  
  
# update centos  
RUN yum -y update  
  
# install required  
RUN yum install -y passenger-standalone make gcc-c++ rsync openssl-devel wget
svn ImageMagick-devel ImageMagick-c++-devel mysql-server mysql-devel openssh-
clients rsync  
  
# install ruby 2  
# note each RUN is on a new instance, so must CD to dir each time  
RUN cd /usr/share && mkdir src && cd src && wget http://cache.ruby-
lang.org/pub/ruby/2.0/ruby-2.0.0-p353.tar.gz  
RUN cd /usr/share/src && tar xvf ruby-2.0.0-p353.tar.gz  
RUN cd /usr/share/src/ruby-2.0.0-p353 && ./configure --prefix=/usr/local
\--enable-shared --disable-install-doc --with-opt-dir=/usr/local  
RUN cd /usr/share/src/ruby-2.0.0-p353 && make && make install  
RUN cd /usr/share/src/ruby-2.0.0-p353/ext/openssl && ruby extconf.rb  
RUN cd /usr/share/src/ruby-2.0.0-p353/ext/openssl && make && make install  
RUN cd /usr/share/src/ruby-2.0.0-p353/ext/zlib && ruby extconf.rb  
RUN cd /usr/share/src/ruby-2.0.0-p353/ext/zlib && make && make install  
  
# install redmine  
RUN cd /var && mkdir www && cd www && svn co
http://svn.redmine.org/redmine/branches/2.4-stable redmine  
RUN cd /var/www/redmine/config && cp database.yml.example database.yml  
RUN cd /var/www/redmine/config && cp configuration.yml.example
configuration.yml  
RUN cd /var/www/redmine && gem install passenger  
RUN cd /var/www/redmine && gem install bundler && bundle install --without
development test postgresql sqlite  
RUN cd /var/www/redmine && rake generate_secret_token  
  
# create default DB  
RUN service mysqld start && mysql &&\  
sleep 3s &&\  
echo "CREATE DATABASE redmine character set utf8; grant all privileges on *.*
to 'root'@'%' with grant option; SHOW DATABASES" | mysql  
  
# migrate database to new version  
RUN service mysqld start && cd /var/www/redmine/ && RAILS_ENV=production rake
db:migrate  
RUN service mysqld start && cd /var/www/redmine/ && RAILS_ENV=production
REDMINE_LANG="en" rake redmine:load_default_data  
  
# expose redmine passenger port  
EXPOSE 3000  
# start mysql & passenger on container run  
CMD /etc/init.d/mysqld start && cd /var/www/redmine && passenger start
--environment production  

