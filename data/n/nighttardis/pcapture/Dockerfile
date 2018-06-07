FROM nginx  
MAINTAINER Philip Henely "henely@gmail.com"  
RUN apt-get update && apt-get -y install wget apt-transport-https  
  
RUN echo "deb
http://download.opensuse.org/repositories/network:/bro/Debian_8.0/ /" >>
/etc/apt/sources.list.d/bro.list  
  
RUN wget -qO -
http://download.opensuse.org/repositories/network:bro/Debian_8.0/Release.key |
apt-key add -  
  
RUN echo "deb https://packages.elastic.co/logstash/2.3/debian stable main" >>
/etc/apt/sources.list.d/logstash.list  
  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add
-  
  
RUN apt-get update && apt-get -y install php5 php5-fpm bro openjdk-7-jre
logstash libgeoip-dev  
  
# Install suricata  
RUN apt-get update && apt-get -y install libpcre3 libpcre3-dbg libpcre3-dev
build-essential autoconf automake libtool libpcap-dev libnet1-dev libyaml-0-2
libyaml-dev zlib1g zlib1g-dev libmagic-dev libcap-ng-dev libjansson-dev pkg-
config  
  
RUN wget http://www.openinfosecfoundation.org/download/suricata-3.1.1.tar.gz  
RUN tar -xvzf suricata-3.1.1.tar.gz  
WORKDIR suricata-3.1.1  
  
RUN ./configure --enable-geoip --prefix=/usr --sysconfdir=/etc
--localstatedir=/var  
RUN make  
RUN make install-full  
  
RUN ldconfig  
  
WORKDIR /  
  
RUN rm -rf suricata-3.1.1 && rm -rf suricata-3.1.1.tar.gz  
  
RUN apt-get update && apt-get -y install sudo  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN echo "cgi.fix_pathinfo=0" >> /etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 5G/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 5G/g"
/etc/php5/fpm/php.ini  
RUN echo "listen=/var/run/php-fpm.sock" >> /etc/php5/fpm/php-fpm.conf  
RUN echo "listen.mode=0666" >> /etc/php5/fpm/php-fpm.conf  
RUN echo "listen.owner=nginx" >> /etc/php5/fpm/php-fpm.conf  
RUN echo "listen.group=nginx" >> /etc/php5/fpm/php-fpm.conf  
RUN echo "user=nginx" >> /etc/php5/fpm/php-fpm.conf  
RUN echo "group=nginx" >> /etc/php5/fpm/php-fpm.conf  
RUN echo "nginx ALL=(ALL) NOPASSWD: /scripts/kill_nginx.sh" >> /etc/sudoers  
  
RUN echo '@load tuning/json-logs' >> /opt/bro/share/bro/site/local.bro  
  
ADD nginx/default /etc/nginx/conf.d/default.conf  
  
ADD suricata/suricata.yaml /etc/suricata/suricata.yaml  
  
RUN mkdir /logstash  
  
ADD logstash/logstash-template.conf /logstash/logstash-template.conf  
  
EXPOSE 80  
RUN mkdir -p /scripts/client_process  
  
ADD scripts/start.sh /scripts/start.sh  
  
ADD scripts/kill_nginx.sh /scripts/kill_nginx.sh  
  
ADD scripts/bro.sh /scripts/client_process/bro.sh  
  
ADD scripts/suricata.sh /scripts/client_process/suricata.sh  
  
ADD scripts/process.sh /scripts/process.sh  
  
ADD scripts/ids_rules_update.sh /scripts/client_process/ids_rules_update.sh  
  
RUN chmod -R 755 /scripts  
  
ADD html/index.php /usr/share/nginx/html/index.php  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
CMD [ "/scripts/start.sh" ]  

