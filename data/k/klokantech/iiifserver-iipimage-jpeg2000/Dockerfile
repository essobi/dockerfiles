FROM debian:jessie  
  
RUN apt-get update && apt-get install -qq -y \  
nginx \  
memcached \  
libfcgi0ldbl \  
libmemcached11 \  
libtiff5 \  
wget \  
libjpeg-turbo-progs \  
python-pip  
  
RUN wget --no-verbose --no-check-certificate \  
-O iiifserver.deb \  
'https://downloads.klokantech.com/iiifserver/iiifserver-1.0.0-262.debian-
jessie.amd64.deb' \  
&& dpkg -i iiifserver.deb \  
&& rm iiifserver.deb \  
&& rm -rf /etc/nginx/sites-enabled/iiifserver.conf \  
&& pip install -q supervisor \  
&& useradd -m iiifserver \  
&& useradd memcached \  
&& chown iiifserver:iiifserver /tmp/iiifserver.log  
  
RUN mkdir -p /data \  
&& mkdir -p /dropzone  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
COPY iiifserver.conf /etc/nginx/sites-available/default  
COPY dropzone.py /usr/bin/dropzone.py  
COPY viewer.html /  
COPY demo.jp2 /  
  
VOLUME /data/  
VOLUME /dropzone/  
  
EXPOSE 80  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

