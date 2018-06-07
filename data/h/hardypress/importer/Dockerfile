FROM ruby:2.4.1-onbuild  
MAINTAINER Claudio Benvenuti <claudio@hardypress.com>  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y \  
curl \  
php5 \  
php5-mysql \  
mysql-client \  
lftp \  
ncftp; \  
rm -rf /var/lib/apt/lists/*;  
  
ENV LANG C.UTF-8  
COPY all_in_one_importer.rb /root/importer/  
COPY dumper.php /root/importer/  
COPY dumper.rb /root/importer/  
COPY ftp_importer.rb /root/importer/  
COPY import_db_dump.rb /root/importer/  
COPY importer.rb /root/importer/  
COPY notify_hardypress.rb /root/importer/  
COPY replace_wp_siteurl.rb /root/importer/  
COPY upload_to_bucket.rb /root/importer/  
COPY wp_config_appendix.php /root/importer/  
  
WORKDIR /root  
CMD ["ruby", "/root/importer/importer.rb"]  
  

