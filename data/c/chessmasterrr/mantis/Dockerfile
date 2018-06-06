FROM chessmasterrr/php:latest  
  
### set values ###  
# see https://www.mantisbt.org/download.php for version number  
ENV MANTIS_VERSION 2.13.1  
# see https://sourceforge.net/projects/mantisbt/files/mantis-stable/{VERSION}/
(click on the i beside the file)  
ENV MANTIS_URL https://sourceforge.net/projects/mantisbt/files/mantis-
stable/${MANTIS_VERSION}/mantisbt-${MANTIS_VERSION}.tar.gz/download  
ENV MANTIS_SHA1 c820ad72ffea0bef9e3538dc0a02d0c533b7e4e2  
  
WORKDIR /var/www/html  
### install application (with Custom Reporter plugin) ###  
RUN set -xe \  
&& wget --no-check-certificate --no-verbose ${MANTIS_URL} -O mantis.tar.gz \  
&& echo "${MANTIS_SHA1} mantis.tar.gz" | sha1sum -c \  
&& tar -xz --strip-components=1 -f mantis.tar.gz \  
&& rm mantis.tar.gz \  
&& wget --no-check-certificate --no-verbose https://github.com/mantisbt-
plugins/CustomReporter/archive/v2.0.0.tar.gz -O customreporter.tar.gz \  
&& mkdir plugins/CustomReporter \  
&& tar -xz --strip-components=1 -f customreporter.tar.gz -C
plugins/CustomReporter/ \  
&& rm customreporter.tar.gz  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  

