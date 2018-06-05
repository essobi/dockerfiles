FROM ubuntu:latest  
MAINTAINER Takumu Uyama  
RUN apt-get update && apt-get -y upgrade && apt-get -y install software-
properties-common tzdata && echo "mysql-server-5.7 mysql-server/root_password
password password" | debconf-set-selections && echo "mysql-server-5.7 mysql-
server/root_password_again password password" | debconf-set-selections  
RUN apt-get install -y php php-cgi libapache2-mod-php php-common php-pear php-
mbstring php-dev mecab libmecab-dev mecab-ipadic-utf8 git apache2 make curl
xz-utils file build-essential sudo mysql-server libmysqlclient-dev php-mysql  
RUN cd /usr/local/src/ && git clone \--depth 1
https://github.com/neologd/mecab-ipadic-neologd.git && cd mecab-ipadic-
neologd/ && echo "yes" | ./bin/install-mecab-ipadic-neologd -n  
RUN cd /usr/local/src/ && git clone https://github.com/rsky/php-mecab.git &&
cd php-mecab/mecab && phpize && ./configure --with-php-config=/usr/bin/php-
config --with-mecab=/usr/bin/mecab-config && make && make test && make install  
RUN echo 'extension=mecab.so' >> /etc/php/7.0/mods-available/mecab.ini && cp
/etc/php/7.0/mods-available/mecab.ini /etc/php/7.0/apache2/conf.d/30-mecab.ini  
COPY ./my.cnf /etc/mysql  
COPY ./php.ini /etc/php/7.0/apache2  
COPY ./CRF++-0.58.tar.gz /usr/local/src  
RUN cd /usr/local/src && tar xvzf CRF++-0.58.tar.gz && cd CRF++-0.58 &&
./configure && make && make install && echo 'include /usr/local/lib' >>
/etc/ld.so.conf && ldconfig  
COPY ./cabocha-0.69.tar.bz2 /usr/local/src  
RUN cd /usr/local/src && tar xvjf cabocha-0.69.tar.bz2 && cd cabocha-0.69 &&
./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8 &&
make && make check && make install && ldconfig  
RUN cd /usr/local/src && git clone https://github.com/y-uti/php-cabocha.git &&
cd php-cabocha && phpize && ./configure && make && make install  
RUN echo 'extension=cabocha.so' >> /etc/php/7.0/mods-available/cabocha.ini &&
cp /etc/php/7.0/mods-available/cabocha.ini
/etc/php/7.0/apache2/conf.d/30-cabocha.ini  

