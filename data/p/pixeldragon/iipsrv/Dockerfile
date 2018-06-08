FROM pixeldragon/fedora-devel:24  
MAINTAINER [Andreas Trawoeger <atrawog@hexaplant.com>]  
  
  
RUN dnf install -y mod_fcgid  
  
RUN mkdir -p /config /data /log /code  
  
RUN chown -R apache.apache /config /data /log /code  
  
RUN cd /code && \  
git clone https://github.com/ruven/iipsrv.git && \  
cd iipsrv && \  
./autogen.sh && \  
./configure --enable-openjpeg && \  
make && \  
mkdir -p /usr/local/iipsrv/ && \  
cp src/iipsrv.fcgi /usr/local/iipsrv/ && \  
chown -R apache.apache /usr/local/iipsrv  
  
ADD config/httpd.conf /etc/httpd/conf/httpd.conf  
  
EXPOSE 80  
CMD ls -lah /run/apache2; rm -f /run/apache2/apache2.pid;/usr/sbin/apachectl
-D FOREGROUND  

