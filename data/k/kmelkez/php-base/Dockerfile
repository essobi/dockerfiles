FROM debian:wheezy  
MAINTAINER Matthieu Keromen <sharoomsorg@gmail.com>  
ENV REFRESHED_AT 2015-06-01  
RUN apt-get update && apt-get install -y wget  
RUN echo "deb http://packages.dotdeb.org wheezy all" >> /etc/apt/sources.list
&& \  
echo "deb-src http://packages.dotdeb.org wheezy all" >> /etc/apt/sources.list
&& \  
echo "deb http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list && \  
echo "deb-src http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list && \  
wget http://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg  
  
RUN apt-get update && apt-get install -y \  
php5-cli \  
php5-gd \  
php5-mysqlnd  
  
ENV TIMEZONE America/Montreal  
  
RUN echo "date.timezone = $TIMEZONE;" >> /etc/php5/cli/php.ini  
  
ENTRYPOINT ["/bin/bash"]  

