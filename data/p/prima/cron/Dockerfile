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
  
RUN apt-get update && apt-get install -y cron && \  
rm -r /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y python python-pip unzip redis-tools
rsync && \  
pip install --upgrade awscli && \  
aws configure set s3.signature_version s3v4 && \  
apt-get purge -y python-pip && \  
rm -r /var/lib/apt/lists/*  
  
# Sovrascrive la versione vecchia solo qua finche' dovremo tenere php di cron
ad una versione precedente  
RUN rm -rf /opt/newrelic-php && \  
curl -o newrelic-php.tar.gz
https://download.newrelic.com/php_agent/archive/7.6.0.201/newrelic-
php5-7.6.0.201-linux.tar.gz && \  
tar xzvf newrelic-php.tar.gz && \  
mv newrelic-php5-* /opt/newrelic-php && \  
rm newrelic-php.tar.gz  
  
# Check that everything was installed correctly  
RUN php -v && wkhtmltopdf --version  
  
COPY crontab/documents_importer /documents_importer  
COPY crontab/facile_export /facile_export  
COPY crontab/chiarezza_export /chiarezza_export  
COPY crontab/streams /streams  
COPY crontab/heartbeat /heartbeat  
COPY crontab/ima_export /ima_export  
COPY crontab/check_gl_ania /check_gl_ania  
COPY crontab/export_month_ania /export_month_ania  
COPY crontab/check_save_paid_not_issued /check_save_paid_not_issued  
  
# Notifier su slack  
COPY crontab/notifier /etc/cron.d/notifier  
  
# permissions su crontab  
RUN chmod 644 /etc/cron.d/*  
  
# run as cron script  
COPY files/run-as-cron.sh /root/run-as-cron.sh  
RUN chmod +x /root/run-as-cron.sh  
COPY files/cronrc /root/cronrc  
RUN chmod +x /root/cronrc  
COPY files/entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
#LOG FOLDER  
RUN mkdir -p /var/log/prima  
  
ENTRYPOINT ["/entrypoint.sh"]  

