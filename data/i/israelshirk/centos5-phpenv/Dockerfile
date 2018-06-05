FROM centos:centos5.11  
RUN echo >> /etc/yum.conf; echo 'multilib_policy=best' >> /etc/yum.conf  
  
RUN yum -y update && rm -rf /var/cache/yum  
  
RUN yum -y install epel-release && rm -rf /var/cache/yum  
RUN yum -y groupinstall "Development Tools" && rm -rf /var/cache/yum  
RUN yum -y install gcc-c++ freetds freetds-devel readline readline-devel
libtidy libtidy-devel libxslt-devel libxslt httpd mod_ssl wget php which git
yum-utils autoconf autoconf213 libgcc httpd-devel libxml2-devel openssl bzip2
bzip2-devel libjpeg libjpeg-devel libXpm libXpm-devel re2c libpng libpng-devel
gd gd-devel git curl zlib-devel openssl-devel curl-devel asciidoc xmlto expat-
devel ncurses ncurses-devel unixODBC-devel postgresql-devel sqlite-devel
aspell-devel net-snmp-devel pcre-devel install gmp gmp-devel libmcrypt
libmcrypt-devel mhash-devel mysql.x86_64 mysql-devel.x86_64 mysql-connector-
odbc && rm -rf /var/cache/yum  
  
RUN yum-builddep php53 && rm -rf /var/cache/yum  
RUN yum-builddep php && rm -rf /var/cache/yum  
  
ENV PATH /usr/local/bin:/usr/local/rbenv/bin:/usr/local/phpenv/bin:$PATH  
ENV RBENV_ROOT /usr/local/rbenv  
ENV PHPENV_ROOT /usr/local/phpenv  
  
RUN git clone https://github.com/sstephenson/rbenv.git /usr/local/rbenv  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bash_profile  
RUN mkdir -p /usr/local/rbenv/plugins  
RUN git clone https://github.com/sstephenson/ruby-build.git
/usr/local/rbenv/plugins/ruby-build  
WORKDIR /usr/local/rbenv/plugins/ruby-build  
RUN ./install.sh  
RUN rbenv install --list  
RUN rbenv install 1.9.3-p551  
  
ENV PATH /usr/local/rbenv/versions/1.9.3-p551/bin/:$PATH  
  
WORKDIR /  
  
RUN git clone git://github.com/phpenv/phpenv.git /usr/local/phpenv  
RUN echo 'eval "$(phpenv init -)"' >> ~/.bash_profile  
RUN mkdir -p /usr/local/phpenv/plugins/  
RUN git clone https://github.com/CHH/php-build.git
/usr/local/phpenv/plugins/php-build  
WORKDIR /usr/local/phpenv/plugins/php-build  
RUN ./install.sh  
WORKDIR /usr/local/phpenv  
RUN git submodule init  
RUN git config --global user.email "you@example.com"; git config --global
user.name "Your Name"  
ADD phpenv.patch phpenv.patch  
RUN git apply --index < phpenv.patch && git add php-ext && git commit -m
"lasdkfj"  
RUN git submodule update  
RUN phpenv install --releases  
  
ENV PHP_AUTOCONF /usr/bin/autoconf-2.13  
ENV PHPENV_DEBUG=true  
ENV LDFLAGS -L/usr/lib64/mysql  
  
ADD phpenv-hooks /usr/local/phpenv/libexec/phpenv-hooks  
  

