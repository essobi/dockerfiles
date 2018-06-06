FROM krallin/ubuntu-tini:14.04  
LABEL maintainer="seti@setadesign.net"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV AUTOMX_VERSION 1.1.2  
  
COPY assets/init.sh /init.sh  
  
RUN apt-get update && \  
apt-get install -y wget apache2 libapache2-mod-wsgi-py3 python3-dateutil
python-ipaddr openssl python3-lxml bsdmainutils dnsutils && \  
mkdir -p /usr/lib/automx && \  
a2enmod wsgi && a2dissite 000-default && \  
wget https://github.com/sys4/automx/archive/v$AUTOMX_VERSION.tar.gz && \  
tar -xf v$AUTOMX_VERSION.tar.gz && \  
cp automx-$AUTOMX_VERSION/src/automx_wsgi.py /usr/lib/automx/ && \  
cp -r automx-$AUTOMX_VERSION/src/automx /usr/lib/python3.4/ && \  
cp automx-$AUTOMX_VERSION/src/automx-test /usr/bin/automx-test && \  
rm -f /var/www/html/index.html && \  
cp -r automx-$AUTOMX_VERSION/src/html /var/www/ && \  
mv /var/www/html/index.html.en /var/www/html/index.html && \  
apt-get clean && \  
rm -rf automx-$AUTOMX_VERSION v$AUTOMX_VERSION.tar.gz \  
/var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chmod 0755 /init.sh  
  
COPY assets/automx.conf /etc/automx.conf  
COPY assets/vhost.conf /etc/apache2/sites-enabled/automx.conf  
  
EXPOSE 80  
  
CMD /init.sh  

