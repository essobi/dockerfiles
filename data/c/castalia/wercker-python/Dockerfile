FROM centos:centos6  
MAINTAINER urasin <urasin2012@gmail.com>  
  
# install tools  
RUN yum update -y  
RUN yum install -y tar  
RUN yum install -y lsof  
RUN yum install -y git  
RUN yum install -y wget  
RUN yum install -y patch  
RUN yum install -y libxml2  
RUN yum install -y libxslt  
  
# install htop  
RUN wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el6.rf.i686.rpm  
RUN rpm -ihv rpmforge-release*.rf.i686.rpm  
RUN yum install -y htop  
  
# install for python build librarys  
RUN yum groupinstall -y development  
RUN yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-
devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel  
  
# install pyenv  
RUN git clone https://github.com/yyuu/pyenv.git /root/.pyenv  
RUN echo 'export PYENV_ROOT=$HOME/.pyenv' >> /root/.bashrc  
RUN echo 'export PATH=$PYENV_ROOT/shims:$PATH' >> /root/.bashrc  
RUN echo 'export PATH=$PYENV_ROOT/bin:$PATH' >> /root/.bashrc  
RUN echo 'eval "$(pyenv init -)"' >> /root/.bashrc  
RUN exec $SHELL  
  
# install python 2.7.9  
RUN /root/.pyenv/bin/pyenv install 2.7.9  
RUN /root/.pyenv/bin/pyenv global 2.7.9  
RUN /root/.pyenv/bin/pyenv rehash  
RUN /root/.pyenv/versions/2.7.9/bin/pip install ansible  
  
# install python 3.4.2  
RUN /root/.pyenv/bin/pyenv install 3.4.2  
  
# rehash and set global python 3.4.2  
RUN /root/.pyenv/bin/pyenv global 3.4.2  
RUN /root/.pyenv/bin/pyenv rehash  
  
# install nginx  
RUN rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-
centos-6-0.el6.ngx.noarch.rpm  
RUN yum install -y nginx  
  
# install mysql  
RUN yum install -y http://dev.mysql.com/get/mysql-community-release-
el6-5.noarch.rpm  
RUN yum install -y mysql-community-server  
  
# install redis  
# RUN wget http://download.redis.io/releases/redis-3.0.3.tar.gz  
# RUN tar xzf redis-3.0.3.tar.gz  
# RUN cd redis-3.0.3  
# RUN make

