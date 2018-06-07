FROM phusion/baseimage:0.9.16  
RUN apt-get update && \  
apt-get -y install \  
wget \  
libxslt1-dev \  
apache2 \  
apache2-threaded-dev && \  
apt-get clean  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Install mod_transform  
WORKDIR /tmp  
RUN wget http://html-xslt.googlecode.com/files/mod-transform-html-xslt-2p2.tgz
&& \  
tar xvzf mod-transform-html-xslt-2p2.tgz  
WORKDIR /tmp/mod-transform-html-xslt-2p2  
RUN ./configure && \  
make && \  
make install  
WORKDIR /tmp  
RUN rm -rf mod-transform-html-xslt-2p2*  
  
# Load mod_transform globally  
RUN echo "LoadModule transform_module
/usr/lib/apache2/modules/mod_transform.so" >> /etc/apache2/apache2.conf  
  
EXPOSE 80  
CMD ["apache2ctl", "-D", "FOREGROUND"]  

