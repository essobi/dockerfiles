FROM ubuntu:16.04  
ADD assets/etc/apt /assets/etc/apt  
  
RUN /bin/bash -c 'ln -fs /assets/etc/apt/sources.list /etc/apt/sources.list'
&& /bin/bash -c 'ln -fs /assets/etc/apt/apt.conf.d/99recommends
/etc/apt/apt.conf.d/99recommends'  
  
RUN apt-get update -qq && apt-get install -y curl software-properties-common
supervisor rsync sudo  
  
# Dockerfile based on:  
# curl
https://raw.githubusercontent.com/atech/postal/master/script/install/ubuntu1604.sh
| sh  
RUN apt-add-repository ppa:brightbox/ruby-ng -y && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 && \  
#add-apt-repository 'deb [arch=amd64,i386,ppc64el]
http://mirrors.coreix.net/mariadb/repo/10.1/ubuntu xenial main' && \  
curl -sL https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key
add -a && \  
add-apt-repository 'deb http://www.rabbitmq.com/debian/ testing main' && \  
apt-get update -qq && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt install -y ruby2.3 ruby2.3-dev build-essential mysql-server
libmysqlclient-dev rabbitmq-server nodejs git nginx && \  
gem install bundler procodile --no-rdoc --no-ri  
  
# Setup mariadb  
RUN mkdir -p /var/run/mysqld && \  
chown -R mysql: /var/run/mysqld && \  
mv /var/lib/mysql /var/lib/mysql.dist  
  
RUN useradd -r -m -d /opt/postal -s /bin/bash postal  
RUN setcap 'cap_net_bind_service=+ep' /usr/bin/ruby2.3  
  
RUN sudo -i -u postal git clone https://github.com/atech/postal
/opt/postal/app  
RUN ln -s /opt/postal/app/bin/postal /usr/bin/postal  
RUN echo "gem 'tzinfo-data'" >> /opt/postal/app/Gemfile  
RUN sudo -i -u postal postal bundle /opt/postal/app/vendor/bundle  
RUN cp /opt/postal/app/resource/nginx.cfg /etc/nginx/sites-available/default
&& \  
mkdir /etc/nginx/ssl/ && \  
openssl req -x509 -newkey rsa:4096 -keyout /etc/nginx/ssl/postal.key -out
/etc/nginx/ssl/postal.crt -days 365 -nodes -subj
"/C=GB/ST=Example/L=Example/O=Example/CN=example.com"  
  
ADD assets /assets  
  
VOLUME
["/var/log/nginx","/var/log/supervisor","/var/log/mysql","/var/lib/mysql","/opt/postal/app/public","/opt/postal/app/log"]  
  
ENTRYPOINT ["/assets/bin/entrypoint"]  

