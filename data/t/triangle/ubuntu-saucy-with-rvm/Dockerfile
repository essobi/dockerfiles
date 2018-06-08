FROM triangle/ubuntu-saucy  
MAINTAINER zs <baloghzsof@gmail.com>  
  
# make sure the package repository is up to date  
RUN apt-get -y update  
RUN apt-get install -y -q software-properties-common  
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) universe"  
RUN apt-get -y update  
  
# install required packages  
RUN apt-get install -y -q build-essential openssl libreadline6 \  
libreadline6-dev curl git-core \  
zlib1g zlib1g-dev libssl-dev libyaml-dev \  
libsqlite3-dev sqlite3 \  
libxml2-dev libxslt-dev autoconf libc6-dev \  
ncurses-dev automake libtool \  
bison subversion pkg-config libmysqlclient-dev \  
libpq-dev make wget unzip \  
git vim nano mysql-client mysql-server gawk \  
libgdbm-dev libffi-dev  
  
# install RVM  
RUN curl -L get.rvm.io | bash -s stable  
  
# add RVM to path  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

