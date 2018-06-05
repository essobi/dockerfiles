FROM million12/nginx-php:php70  
MAINTAINER Richard WU <taipeiwu@yahoo.com.tw>  
  
ENV DB_USER=cactiuser \  
DB_PASS=password \  
DB_ADDRESS=127.0.0.1 \  
SPINE_VERSION=1.1.0 \  
CACTI_COMMIT_HASH=release/1.1.0 \  
TIMEZONE=UTC  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y rrdtool mariadb-devel cronie \  
net-snmp net-snmp-utils autoconf automake gcc-core gzip \  
help2man libtool make net-snmp-devel m4 openssl-devel \  
dos2unix wget file php70-php-ldap php70-php-snmp && \  
git clone https://github.com/Cacti/cacti.git /cacti/ && \  
cd /cacti && git checkout ${CACTI_COMMIT_HASH} && \  
curl -o /tmp/cacti-spine.tgz http://www.cacti.net/downloads/spine/cacti-
spine-${SPINE_VERSION}.tar.gz && \  
mkdir -p /tmp/spine && \  
tar zxvf /tmp/cacti-spine.tgz -C /tmp/spine --strip-components=1 && \  
rm -f /tmp/cacti-spine.tgz && \  
cd /tmp/spine/ && ./configure && make && make install && \  
rm -rf /tmp/spine && \  
yum remove -y gcc mariadb-devel net-snmp-devel && \  
yum clean all  
  
COPY container-files /  
  
EXPOSE 80 81 443

