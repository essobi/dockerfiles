FROM mysql:5.7.21  
ENV MYSQL_VERSION 5.7.21  
ENV TRANSACTD_VERSION 3.8.1  
ENV TRANSACTD_DOWNLOAD_MD5 10e007a3ce71f81546dff31daf09bc2c  
ENV TRANSACTD_UTILITY_VERSION 3.8.0  
ENV TRANSACTD_UTILITY_DOWNLOAD_MD5 af76784ec10cabeecc0ad254d5d0ad3b  
  
# plugin-dir: mysqld --verbose --help | grep ^plugin-dir  
RUN set -ex \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y wget locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O transactd.tar.gz
"http://www.bizstation.jp/al/transactd/download/transactd-${TRANSACTD_VERSION}/transactd-
linux-x86_64-${TRANSACTD_VERSION}_mysql-${MYSQL_VERSION}.tar.gz" \  
&& echo "${TRANSACTD_DOWNLOAD_MD5} *transactd.tar.gz" | md5sum -c - \  
&& tar xzf transactd.tar.gz -C /usr/lib/mysql/plugin/ --strip-components=1
transactd-
linux-x86_64-${TRANSACTD_VERSION}_mysql-${MYSQL_VERSION}/libtransactd.so \  
&& rm transactd.tar.gz \  
&& wget -O transactd-client-uty.tar.gz
"http://www.bizstation.jp/al/transactd/download/transactd-client/transactd-
client-uty-linux-x86_64-${TRANSACTD_UTILITY_VERSION}.tar.gz" \  
&& echo "${TRANSACTD_UTILITY_DOWNLOAD_MD5} *transactd-client-uty.tar.gz" |
md5sum -c - \  
&& mkdir /root/utility \  
&& tar xzf transactd-client-uty.tar.gz -C /root/utility --strip-components=1 \  
&& cd /root/utility \  
&& ./install_client.sh \  
&& ldconfig \  
&& /bin/echo -e '[mysqld]\nplugin-load=transactd=libtransactd.so' >
/etc/mysql/conf.d/transactd.cnf \  
&& apt-get purge -y --auto-remove wget \  
&& echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen ja_JP.UTF-8  
  
ENV LC_ALL ja_JP.UTF-8  

