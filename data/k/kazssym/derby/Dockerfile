# Dockerfile for Apache Derby 10.13  
# Copyright (C) 2017 Kaz Nishimura  
#  
# Copying and distribution of this file, with or without modification,  
# are permitted in any medium without royalty provided the copyright  
# notice and this notice are preserved. This file is offered as-is,  
# without any warranty.  
FROM openjdk:8-jre  
  
WORKDIR /opt/apache/derby  
  
ENV DERBY_VERSION=10.13.1.1 \  
DERBY_PGPSIGNER=F5CDB4E5ACED962DAC68952266C02FE18B5C5237  
  
RUN set -x && \  
wget -q http://www-us.apache.org/dist/db/derby/db-derby-$DERBY_VERSION/db-
derby-$DERBY_VERSION-lib.tar.gz && \  
export GNUPGHOME=`mktemp -d` && \  
(echo disable-ipv6) > $GNUPGHOME/dirmngr.conf && \  
gpg -q --recv-keys $DERBY_PGPSIGNER && \  
wget -q -O - http://www-us.apache.org/dist/db/derby/db-
derby-$DERBY_VERSION/db-derby-$DERBY_VERSION-lib.tar.gz.asc | gpg -q --verify
- db-derby-$DERBY_VERSION-lib.tar.gz && \  
rm -rf $GNUPGHOME && \  
gzip -d < db-derby-$DERBY_VERSION-lib.tar.gz | tar -x --strip-components=1
--no-same-owner && \  
rm db-derby-$DERBY_VERSION-lib.tar.gz  
  
CMD ["java", "-jar", "/opt/apache/derby/lib/derbynet.jar", "start"]  

