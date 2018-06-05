FROM debian:jessie  
MAINTAINER Quadeare <lacrampe.florian@gmail.com>  
  
# Export TERM  
RUN export TERM=xterm  
  
# Setup dependencies  
RUN echo "deb http://http.debian.net/debian jessie main\n\  
deb-src http://http.debian.net/debian jessie main\n\  
deb http://http.debian.net/debian jessie-updates main\n\  
deb-src http://http.debian.net/debian jessie-updates main\n\  
deb http://security.debian.org jessie/updates main\n\  
deb-src http://security.debian.org jessie/updates main\n\  
" > /etc/apt/sources.list  
  
# Install dependencies  
RUN apt-get update  
  
# Get all software  
RUN apt-get install -y wget apache2 php5 php5-mcrypt php5-gd php5-sqlite
php5-mysql php5-pgsql supervisor git unzip zip libav-tools imagemagick
apache2-utils pure-ftpd  
RUN apt-get build-dep -y aria2 pure-ftpd  
  
# Install pure-ftpd  
RUN mkdir /tmp/pure-ftpd/ && \  
cd /tmp/pure-ftpd/ && \  
apt-get source pure-ftpd && \  
cd pure-ftpd-* && \  
sed -i '/^optflags=/ s/$/ --without-capabilities/g' ./debian/rules && \  
dpkg-buildpackage -b -uc  
  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd-common*.deb  
RUN apt-get -y install openbsd-inetd  
RUN dpkg -i /tmp/pure-ftpd/pure-ftpd_*.deb  
  
# Prevent pure-ftpd upgrading  
RUN apt-mark hold pure-ftpd pure-ftpd-common  
  
# Clean apt-get  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install aria2  
RUN mkdir -p /tmp/aria2-compilation  
WORKDIR /tmp/aria2-compilation  
RUN wget
https://github.com/aria2/aria2/releases/download/release-1.23.0/aria2-1.23.0.tar.xz  
RUN tar xf aria2-1.23.0.tar.xz && rm aria2-1.23.0.tar.xz  
WORKDIR /tmp/aria2-compilation/aria2-1.23.0  
RUN ./configure  
RUN make && make install  
  
# Enable apache2 modules  
RUN a2enmod ssl && a2enmod rewrite  
  
# Fix php output_buffering  
RUN sed -i 's/output_buffering = 4096/output_buffering = Off/g'
/etc/php5/apache2/php.ini  
RUN rm -rf /var/www/html  
  
# Install pydio  
WORKDIR "/var/www/pydio"  
RUN wget http://netix.dl.sourceforge.net/project/ajaxplorer/pydio/stable-
channel/6.2.2/pydio-core-6.2.2.tar.gz  
RUN tar xf pydio-core-6.2.2.tar.gz  
RUN cp -a pydio-core-6.2.2/* .  
RUN rm -rf pydio-core-6.2.2/ pydio-core-6.2.2.tar.gz  
  
# Install aria2 web-ui  
WORKDIR "/var/www/aria2-webui"  
RUN git clone https://github.com/ziahamza/webui-aria2.git ./  
RUN touch /etc/apache2/.htpasswd  
  
# Add configs files  
ADD ./extra-data/mcrypt.ini /etc/php5/apache2/conf.d/mcrypt.ini  
ADD ./extra-data/000-default.conf /etc/apache2/sites-
available/000-default.conf  
ADD ./extra-data/.htaccess /var/www/pydio/.htaccess  
ADD ./extra-data/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD ./extra-data/configuration.js /var/www/aria2-webui/configuration.js_bak  
ADD ./extra-data/start.sh /start.sh  
ADD ./extra-data/add-user.sh /add-user.sh  
ADD ./extra-data/remove-user.sh /remove-user.sh  
ADD ./extra-data/aria2.conf /aria2.conf_bak  
ADD ./extra-data/envvars /etc/apache2/envvars  
  
# Add bash script on bash  
RUN ln -s /remove-user.sh /usr/bin/remove-user  
RUN ln -s /add-user.sh /usr/bin/add-user  
  
# Volume  
RUN rm -rf /var/www/pydio/data/files  
RUN ln -s /downloads /var/www/pydio/data/files  
  
# Setup FTP  
RUN groupadd ftpgroup  
RUN useradd -g ftpgroup -d /dev/null -s /etc ftpuser  
RUN echo "no" > /etc/pure-ftpd/conf/PAMAuthentication  
RUN echo "yes" > /etc/pure-ftpd/conf/DontResolve  
WORKDIR "/etc/pure-ftpd/auth/"  
RUN ln -s ../conf/PureDB 50puredb  
RUN touch /etc/pure-ftpd/pureftpd.passwd  
  
# Fix rights  
WORKDIR "/var/www"  
RUN chown -R ftpuser:ftpgroup /var/www  
RUN chmod 644 /etc/pure-ftpd/pureftpd.passwd  
  
# Volume  
VOLUME ["/downloads", "/etc/pure-ftpd/"]  
  
# Expose ports  
EXPOSE 80  
EXPOSE 21  
EXPOSE 6800  
EXPOSE 30000-30009  
CMD ["/start.sh"]  

