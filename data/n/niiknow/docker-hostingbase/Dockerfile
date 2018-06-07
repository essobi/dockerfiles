FROM hyperknot/baseimage16:1.0.4  
  
LABEL maintainer="noogen <friends@niiknow.org>"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 TERM=xterm
container=docker  
  
RUN cd /tmp \  
&& apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys 4F4EA0AAE5267A6C
\  
&& add-apt-repository -y ppa:pinepain/libv8 \  
&& curl -s -o /tmp/couchbase-release-1.0-4-amd64.deb
http://packages.couchbase.com/releases/couchbase-release/couchbase-
release-1.0-4-amd64.deb \  
&& dpkg -i /tmp/couchbase-release-1.0-4-amd64.deb \  
&& add-apt-repository -y ppa:couchdb/stable \  
&& apt-add-repository -y ppa:ondrej/php \  
&& apt-get update && apt-get -y \--no-install-recommends upgrade \  
&& apt-get -y \--no-install-recommends \--allow-unauthenticated install wget
curl unzip nano vim rsync apt-transport-https openssh-client openssh-server \  
sudo tar git apt-utils software-properties-common build-essential python-dev
tcl openssl libpcre3 dnsmasq ca-certificates libpcre3-dev re2c \  
libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev libmagickwand-dev
procps imagemagick netcat libv8-6.6-dev pkg-config \  
mcrypt pwgen language-pack-en-base libicu-dev g++ cpp libglib2.0-dev incron
libcouchbase-dev libcouchbase2-libevent \  
php7.2-dev php-pear php-xml php7.2-xml php5.6-dev php5.6-xml php7.0-dev
php7.0-xml php7.1-dev php7.1-xml \  
libc6 libcurl3 libgcc1 libgssapi-krb5-2 liblttng-ust0 libssl1.0.0 libstdc++6
libunwind8 libuuid1 zlib1g \  
&& systemctl disable incron \  
&& echo 'root' >> /etc/incron.allow \  
&& dpkg \--configure -a && ls -la /opt/libv8-6.6 && pecl channel-update
pecl.php.net \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /core \  
&& rm -rf /tmp/* \  
&& find /etc/service/ -name "down" -exec rm -f {} \;  
  
COPY rootfs/. /  
  
RUN cd /tmp \  
&& chmod +x /etc/service/sshd/run \  
&& chmod +x /usr/bin/backup-creds.sh \  
&& chmod +x /etc/service/incrond/run \  
&& /usr/bin/switch-php.sh "7.2" \  
&& cd /tmp && curl -sL https://pecl.php.net/get/pcs > pcs.tgz && tar -xf
pcs.tgz && cd pcs-* && phpize && ./configure && make && make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/igbinary > igbinary.tgz && tar
-xf igbinary.tgz && cd igbinary-* && phpize && ./configure && make && make
install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/couchbase > couchbase.tgz &&
tar -xf couchbase.tgz && cd couchbase-* && phpize && ./configure && make &&
make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/imagick > imagick.tgz && tar
-xf imagick.tgz && cd imagick-* && phpize && ./configure && make && make
install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/v8js > v8js.tgz && tar -xf
v8js.tgz && cd v8js-* && phpize && LDFLAGS="-lstdc++" ./configure
\--with-v8js=/opt/libv8-6.6 && make && make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/v8 > v8.tgz && tar -xf v8.tgz
&& cd v8-* && phpize && ./configure \--with-v8=/opt/libv8-6.6 && make && make
install \  
&& rm -rf /tmp/* \  
&& /usr/bin/switch-php.sh "5.6" \  
&& cd /tmp && curl -sL https://pecl.php.net/get/pcs > pcs.tgz && tar -xf
pcs.tgz && cd pcs-* && phpize && ./configure && make && make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/igbinary > igbinary.tgz && tar
-xf igbinary.tgz && cd igbinary-* && phpize && ./configure && make && make
install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/couchbase > couchbase.tgz &&
tar -xf couchbase.tgz && cd couchbase-* && phpize && ./configure && make &&
make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/imagick > imagick.tgz && tar
-xf imagick.tgz && cd imagick-* && phpize && ./configure && make && make
install \  
&& rm -rf /tmp/* \  
&& /usr/bin/switch-php.sh "7.0" \  
&& cd /tmp && curl -sL https://pecl.php.net/get/pcs > pcs.tgz && tar -xf
pcs.tgz && cd pcs-* && phpize && ./configure && make && make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/igbinary > igbinary.tgz && tar
-xf igbinary.tgz && cd igbinary-* && phpize && ./configure && make && make
install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/couchbase > couchbase.tgz &&
tar -xf couchbase.tgz && cd couchbase-* && phpize && ./configure && make &&
make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/imagick > imagick.tgz && tar
-xf imagick.tgz && cd imagick-* && phpize && ./configure && make && make
install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/v8js > v8js.tgz && tar -xf
v8js.tgz && cd v8js-* && phpize && LDFLAGS="-lstdc++" ./configure
\--with-v8js=/opt/libv8-6.6 && make && make install \  
&& rm -rf /tmp/* \  
&& /usr/bin/switch-php.sh "7.1" \  
&& cd /tmp && curl -sL https://pecl.php.net/get/pcs > pcs.tgz && tar -xf
pcs.tgz && cd pcs-* && phpize && ./configure && make && make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/igbinary > igbinary.tgz && tar
-xf igbinary.tgz && cd igbinary-* && phpize && ./configure && make && make
install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/couchbase > couchbase.tgz &&
tar -xf couchbase.tgz && cd couchbase-* && phpize && ./configure && make &&
make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/imagick > imagick.tgz && tar
-xf imagick.tgz && cd imagick-* && phpize && ./configure && make && make
install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/v8js > v8js.tgz && tar -xf
v8js.tgz && cd v8js-* && phpize && LDFLAGS="-lstdc++" ./configure
\--with-v8js=/opt/libv8-6.6 && make && make install \  
&& cd /tmp && curl -sL https://pecl.php.net/get/v8 > v8.tgz && tar -xf v8.tgz
&& cd v8-* && phpize && ./configure \--with-v8=/opt/libv8-6.6 && make && make
install \  
&& curl -s -o /tmp/python-support_1.0.15_all.deb
https://launchpadlibrarian.net/109052632/python-support_1.0.15_all.deb \  
&& dpkg -i /tmp/python-support_1.0.15_all.deb \  
&& apt-key adv \--recv-keys \--keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 \  
&& add-apt-repository 'deb [arch=amd64,i386]
http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.2/ubuntu xenial main' \  
&& apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 \--recv
2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 \  
&& echo 'deb [arch=amd64,i386] http://repo.mongodb.org/apt/ubuntu
xenial/mongodb-org/3.6 multiverse' \  
| sudo tee /etc/apt/sources.list.d/mongodb-3.6.list \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update && apt-get -y \--no-install-recommends upgrade \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | gpg \--dearmor >
microsoft.gpg \  
&& mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \  
&& echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-
ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list \  
&& apt-get -y \--no-install-recommends \--allow-unauthenticated install
oracle-java8-installer oracle-java8-set-default \  
&& dpkg \--configure -a \  
&& echo "\n\nJAVA_HOME=/usr/lib/jvm/java-8-oracle\nexport JAVA_HOME\n" >>
/root/.profile \  
&& curl -sS https://getcomposer.org/installer | php -- \--install-
dir=/usr/local/bin \--filename=composer \  
&& curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \  
&& rm -rf /tmp/* \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/cache/oracle-jdk8-installer  
  
ENV DEBIAN_FRONTEND=teletype  
  
VOLUME ["/backup"]  
  
CMD ["/sbin/my_init"]  

