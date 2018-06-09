FROM debian:7.9  
MAINTAINER taka2063  
  
WORKDIR /root/  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get -y install wget  
RUN echo "deb http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list.d/dotdeb.list && \  
echo "deb-src http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list.d/dotdeb.list && \  
echo "deb http://httpredir.debian.org/debian/ wheezy-backports main" >>
/etc/apt/sources.list.d/dotdeb.list && \  
wget http://www.dotdeb.org/dotdeb.gpg -O- |apt-key add -  
RUN apt-get update  
RUN apt-get -y install chkconfig net-tools tar curl vim git sudo  
RUN apt-get -y install php5 php5-curl php5-gd php5-mysql php5-imagick  
RUN apt-get -y install nodejs nodejs-legacy  
RUN wget http://www.npmjs.org/install.sh --no-check-certificate && \  
sh install.sh && rm install.sh  
RUN npm install -g gulp  
ENV DEBIAN_FRONTEND dialog  
  
# 日本時間  
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
# ttyコメントアウト  
RUN sed -i -e 's/^\\([1-6]:.\\+\\)/#\1/g' /etc/inittab  
  
#COPY asset/ttystop /etc/init.d/  
#RUN chkconfig --add ttystop && chkconfig ttystop on  
# composer  
RUN curl -s http://getcomposer.org/installer | php && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer  
  
RUN composer global require hirak/prestissimo  
RUN echo "export PATH=${PATH}:.:${HOME}/.composer/vendor/bin" >> ~/.bashrc  
  
WORKDIR /var/www  
  
EXPOSE 80  
CMD ["/sbin/init", "3"]  

