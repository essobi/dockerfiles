FROM ubuntu:14.04  
MAINTAINER Natanael Arndt <arndt@informatik.uni-leipzig.de>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# See also: https://natanael.arndt.xyz/2017/06/23/Forward-SSH-Authentication-
To-Docker-Container  
ENV SSH_AUTH_SOCK /var/run/ssh-agent.sock  
  
# OntoWiki Site Extension configuration  
ENV OW_SITE_MODEL "http://pfarrerbuch.aksw.org/"  
# install some basic packages  
# install the nginx server with PHP  
# install virtuoso  
RUN apt-get update && apt-get install -y \  
git make curl \  
nginx-light \  
php5-fpm php5-odbc php5-curl php5-cli \  
logrotate \  
raptor-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
# TODO connect using docker-compose and tenforce-image  
ADD virtuoso-opensource_7.1_amd64.deb /  
RUN dpkg -i virtuoso-opensource_7.1_amd64.deb  
  
RUN ln -s /usr/bin/isql-v /usr/bin/isql-vt  
  
# clone ontowiki and get its dependencies  
RUN git clone https://github.com/AKSW/pfarrerbuch.de.git /var/www/  
RUN cd /var/www/ && make deploy && make custom  
ADD ow-config.ini /var/www/config.ini  
  
# configure the ontowiki site for nginx  
ADD nginx.conf /etc/nginx/sites-available/ontowiki.conf  
RUN rm /etc/nginx/sites-enabled/default  
RUN ln -s /etc/nginx/sites-available/ontowiki.conf /etc/nginx/sites-enabled/  
  
# configure odbc for virtuoso  
ADD odbc.ini /etc/  
  
ADD virtuoso.ini.patch /virtuoso.ini.patch  
RUN patch /var/lib/virtuoso/db/virtuoso.ini < virtuoso.ini.patch  
ADD dump_one_graph.virtuoso.sql /dump_one_graph.virtuoso.sql  
  
ADD 30-memory_limit.ini /etc/php5/fpm/conf.d/30-memory_limit.ini  
  
# Configure logrotate  
ADD ontowiki-logrotate /etc/logrotate.d/ontowiki  
ADD virtuoso-logrotate /etc/logrotate.d/virtuoso  
# TODO fix filepermissions for log directories  
# Add startscript and start  
ADD start.sh /start.sh  
ADD ow-docker.fig /ow-docker.fig  
CMD ["/bin/bash", "/start.sh"]  
  
# expose the HTTP port to the outer world  
EXPOSE 80  

