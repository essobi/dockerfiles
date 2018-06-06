FROM java:7  
MAINTAINER Sebastin Lastra <sebastian.lastra@cursor.cl>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# MYSQL  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server  
RUN sed -i -e "s/^bind-address\s*=\s*\\(.*\\)/#bind-address = \1/"
/etc/mysql/my.cnf  
RUN sed -i -e "s/\\(\\[mysqld\\]\\)/\1\ncharacter-set-server = utf8/g"
/etc/mysql/my.cnf  
RUN sed -i -e "s/\\(\\[client\\]\\)/\1\ndefault-character-set = utf8/g"
/etc/mysql/my.cnf  
RUN sed -i -e "s/\\(\\[mysqldump\\]\\)/\1\ndefault-character-set = utf8/g"
/etc/mysql/my.cnf  
RUN sed -i -e "s/\\(\\[mysql\\]\\)/\1\ndefault-character-set = utf8/g"
/etc/mysql/my.cnf  
RUN service mysql start  
  
# PLAY  
ENV PLAY_VERSION 2.2.6  
RUN apt-get install -y wget unzip git  
RUN wget -q
https://downloads.typesafe.com/play/${PLAY_VERSION}/play-${PLAY_VERSION}.zip \  
&& unzip -q play-${PLAY_VERSION}.zip \  
&& rm play-${PLAY_VERSION}.zip \  
&& ln -s /play-${PLAY_VERSION}/play /usr/local/bin/

