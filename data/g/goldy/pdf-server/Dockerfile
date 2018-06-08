FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DOC_DIR /var/www/pdf-server/docs/  
  
# install apache  
RUN apt-get update && apt-get -y install apache2 \  
xapian-omega \  
poppler-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm /etc/apache2/sites-enabled/*  
  
# install pyentrypoint  
RUN apt-get update && apt-get -y install python-pip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get -y install python-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install -U pip  
  
RUN pip install -U pyentrypoint==0.5.0 \  
pypdfocr==0.9.1  
  
# Dependancy for OCR  
RUN apt-get update && apt-get -y install tesseract-ocr \  
'tesseract-ocr-*' \  
ghostscript \  
poppler-utils \  
imagemagick \  
fdupes \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD assets/entrypoint* /  
ADD assets/set_access /usr/local/bin/set_access  
ADD assets/omega-apache /etc/apache2/sites-enabled/omega.conf.tpl  
ADD assets/xapian-update /usr/local/bin/xapian-update  
ADD assets/run-ocr /usr/local/bin/run-ocr  
ADD assets/index.html /var/www/pdf-server/index.html  
ADD assets/ocr-config.yml /var/local/etc/ocr-config.yml  
  
RUN mkdir -p /var/www/pdf-server/docs/ocr \  
/var/www/pdf-server/docs/upload \  
/var/www/pdf-server/docs/raws \  
/var/lock/apache2 \  
/var/local/upload \  
&& chown -R www-data:www-data /var/www/pdf-server/ \  
/var/lock/apache2 \  
/var/lib/xapian-omega \  
/var/local/upload  
  
RUN chmod -R +x /usr/local/bin  
  
# Apache env and setup  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN a2enmod cgi  
  
VOLUME /var/lib/xapian-omega  
VOLUME /var/www/pdf-server/docs  
  
ENTRYPOINT ["pyentrypoint"]  

