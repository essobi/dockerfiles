FROM prima/php:7.2.5-2  
ENV
WKHTMLTOPDF_SHA256=049b2cdec9a8254f0ef8ac273afaf54f7e25459a273e27189591edc7d7cf29db  
  
RUN apt-get update && \  
apt-get install -y xz-utils libxext6 libfontconfig1 libxrender-dev && \  
curl -L -o /opt/wkhtmltox.tar.xz
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
cd /opt && \  
echo "${WKHTMLTOPDF_SHA256} wkhtmltox.tar.xz" | sha256sum -c - && \  
tar xf /opt/wkhtmltox.tar.xz -C /opt/ && \  
cp /opt/wkhtmltox/bin/* /usr/local/bin && \  
chmod +x /usr/local/bin/wkhtml*  
  
RUN apt-get update && apt-get install -y python python-pip unzip mysql-client
rsync && \  
pip install --upgrade awscli && \  
aws configure set s3.signature_version s3v4 && \  
apt-get purge -y python-pip && \  
rm -r /var/lib/apt/lists/*  
  
# Check that everything was installed correctly  
RUN php -v && php-fpm -v && wkhtmltopdf --version  
  
RUN rm -rf /usr/local/etc/fpm.d/* /usr/local/etc/php-fpm.d/  
  
COPY files/fpm.d/* /usr/local/etc/fpm.d/  
COPY files/entrypoint.sh /entrypoint.sh  
COPY files/prima.ini /usr/local/etc/php/conf.d/prima.ini  
  
ENV FPM_MAX_CHILDREN=5 \  
FPM_START_SERVERS=2 \  
FPM_MIN_SPARE_SERVERS=1 \  
FPM_MAX_SPARE_SERVERS=2 \  
PHP_MAX_EXECUTION_TIME=15  
CMD ["php-fpm", "--nodaemonize"]  

