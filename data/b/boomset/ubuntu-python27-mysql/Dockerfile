FROM ubuntu:xenial  
MAINTAINER Ülgen Sarıkavak <ulgensrkvk@gmail.com>  
  
# Set locale  
RUN apt-get clean && apt-get update && apt-get install locales && locale-gen
en_US en_US.UTF-8 && update-locale  
  
# MySQL Setup  
RUN echo "mysql-server-5.5 mysql-server/root_password password root" |
debconf-set-selections && \  
echo "mysql-server-5.5 mysql-server/root_password_again password root" |
debconf-set-selections  
  
# Install packages  
RUN apt-get update && apt-get install python-pip python-dev libmysqlclient-dev
mysql-server rabbitmq-server wget git -y && \  
apt-get autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget -c https://github.com/git-lfs/git-lfs/releases/download/v1.5.5/git-
lfs-linux-amd64-1.5.5.tar.gz  
RUN tar -xzf git-lfs-linux-amd64-1.5.5.tar.gz  
RUN cd git-lfs-1.5.5/ && ./install.sh  
  
RUN pip install virtualenv  

