FROM centos:6.7  
ENV RUBY_VERSION 2.2.2  
ENV MYSQL_RPM_VERSION mysql-community-release-el6-5.noarch.rpm  
  
# Install packages for building ruby  
RUN yum -y update  
RUN yum install -y git gcc gcc-c++ make tar wget openssl-devel readline-devel
sqlite-devel zlib zlib-devel file  
RUN yum install -y libcurl-devel libyaml-devel libffi-devel bzip2 autoconf
automake libtool bison libxml2-devel libxslt-devel  
  
# Install rbenv and ruby-build  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN ./root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/bin:$PATH  
RUN echo 'export PATH=/root/.rbenv/bin:$PATH' >> /root/.bashrc  
RUN echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
  
# Install ruby  
ENV CONFIGURE_OPTS --disable-install-doc  
RUN rbenv install $RUBY_VERSION  
RUN rbenv global $RUBY_VERSION  
  
# Install Bundler for ruby  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
RUN rbenv exec gem install bundler  
  
# Install mysql  
RUN yum install -y http://repo.mysql.com/$MYSQL_RPM_VERSION  
RUN yum install -y mysql-community-server mysql-community-devel  
  
ENV MYSQL_ROOT_PASSWORD 'password'  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
  
EXPOSE 3306  
RUN . /entrypoint.sh mysqld --datadir=/var/lib/mysql --user=mysql  
  
# Install packages for poltergeist  
RUN cd /usr/local/src/ && wget
https://phantomjs.googlecode.com/files/phantomjs-1.9.2-linux-x86_64.tar.bz2  
RUN tar jxfv /usr/local/src/phantomjs-1.9.2-linux-x86_64.tar.bz2  
RUN cp phantomjs-1.9.2-linux-x86_64/bin/phantomjs /usr/bin/  
  
# yum clean  
RUN yum clean all  
  

