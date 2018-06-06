FROM ubuntu:14.04.4  
MAINTAINER Olexander Kutsenko <olexander.kutsenko@gmail.com>  
  
# Install Dependencies  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y software-properties-common python-software-properties \  
git git-core vim nano mc nginx tmux curl unzip zip wget \  
python-dev python-setuptools postfix \  
apache2-utils tmux apt-transport-https supervisor  
COPY configs/supervisor/*.conf /etc/supervisor/conf.d/  
COPY configs/nginx/default /etc/nginx/sites-available/default  
RUN easy_install pip  
RUN echo "postfix postfix/mailname string elk.hostname.com" | debconf-set-
selections  
RUN echo "postfix postfix/main_mailer_type string 'ELK'" | debconf-set-
selections  
  
# Install locale  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Install Java 8  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
# Accept license non-interactive  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer \  
oracle-java8-set-default  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" | tee -a /etc/environment  
RUN export JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
# SSH service  
RUN apt-get install -y openssh-server openssh-client  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
#change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> tee -a /etc/profile  
  
#Generate SSL Certificates  
RUN mkdir -p /etc/pki/tls  
RUN mkdir -p /etc/pki/tls/private/  
RUN mkdir -p /etc/pki/tls/certs  
RUN sed -i 's/# Extensions for a typical CA/subjectAltName = IP: 127.0.0.1/g'
/etc/ssl/openssl.cnf  
RUN openssl req -config /etc/ssl/openssl.cnf -x509 -days 3650 -batch -nodes
-newkey rsa:2048 -keyout /etc/pki/tls/private/logstash-forwarder.key -out
/etc/pki/tls/certs/logstash-forwarder.crt  
  
# Configs bash start  
COPY configs/autostart.sh /root/autostart.sh  
COPY configs/bash.bashrc /etc/bash.bashrc  
RUN chmod +x /root/autostart.sh  
  
# Add colorful command line  
RUN echo "force_color_prompt=yes" >> ~/.bashrc  
RUN echo "export
PS1='${debian_chroot:+($debian_chroot)}\\[\033[01;31m\\]\u\\[\033[01;33m\\]@\\[\033[01;36m\\]\h
\\[\033[01;33m\\]\w \\[\033[01;35m\\]\$ \\[\033[00m\\]'" >> .bashrc  
  
#Install Elasticsearch  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add
-  
RUN echo "deb http://packages.elastic.co/elasticsearch/2.x/debian stable main"
| tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list  
RUN apt-get update  
RUN apt-get -y install elasticsearch  
RUN echo "network.host: localhost" | tee -a
/etc/elasticsearch/elasticsearch.yml  
RUN echo "MAX_MAP_COUNT=" | tee -a /etc/default/elasticsearch  
RUN mkdir -p /usr/share/elasticsearch/config  
COPY configs/elasticsearch/elasticsearch.yml /usr/share/elasticsearch/config  
COPY configs/elasticsearch/logging.yml /usr/share/elasticsearch/config  
  
#Install Kibana  
RUN echo "deb http://packages.elastic.co/kibana/4.6/debian stable main" | tee
-a /etc/apt/sources.list.d/kibana-4.x.list  
RUN apt-get update  
RUN apt-get -y install kibana  
RUN echo 'server.host: localhost' | tee -a /opt/kibana/config/kibana.yml  
RUN service kibana start  
RUN htpasswd -b -c /etc/nginx/htpasswd.users admin admin  
RUN service nginx restart  
  
#Install Logstash  
RUN echo 'deb http://packages.elastic.co/logstash/2.2/debian stable main' |
tee /etc/apt/sources.list.d/logstash-2.2.x.list  
RUN apt-get update  
RUN apt-get install logstash -y  
COPY configs/logstash/* /etc/logstash/conf.d/  
COPY configs/supervisor/*.conf /etc/supervisor/conf.d/  
  
# Instal ElasticAlert  
COPY configs/alerts.zip /opt/alerts.zip  
RUN unzip -d /opt/elastalert /opt/alerts.zip  
RUN rm /opt/alerts.zip  
  
# etcKeeper  
COPY configs/etckeeper.sh /root  
COPY configs/etckeeper-hook.sh /root/etckeeper  
RUN /root/etckeeper.sh  
RUN rm /etc/apt/sources.list.d/*  
RUN apt-get update  
  
# Open ports  
EXPOSE 80 5044

