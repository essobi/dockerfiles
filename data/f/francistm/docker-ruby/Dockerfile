FROM ubuntu:14.04  
MAINTAINER FrancisTM <francis.tm@gmail.com>  
LABEL Version="1.0.0" Description="rvm based Ruby environment, with Nginx
support"  
  
# Create config file directory  
RUN mkdir -p /var/run/sshd  
ADD ./supervisord.conf /etc/  
  
RUN apt-get update -qq  
RUN apt-get install -y curl patch gawk g++ gcc make libc6-dev \  
patch libreadline6-dev zlib1g-dev libssl-dev libyaml-dev \  
libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev \  
automake libtool bison pkg-config libffi-dev git python-pip \  
libmysqlclient-dev wget imagemagick nodejs nginx openssh-server  
  
# Install OpenSSH  
RUN mkdir -p /var/run/sshd  
  
# Install Supervisor  
RUN pip install -U supervisor  
  
# Create `site` user  
RUN useradd -m -s /bin/bash site  
  
USER site  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable --ruby=2.2.1 --gems=bundler  
  
# Expose ports & run supervisor  
USER root  
EXPOSE 22 80  
ENTRYPOINT /usr/local/bin/supervisord -n -l /var/log/supervisord.log \  
-c /etc/supervisord.conf  

