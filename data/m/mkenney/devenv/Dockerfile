#  
# MIT License  
#  
# Copyright (c) 2017 Michael Kenney  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
#  
  
FROM mkenney/devenv-base:latest  
  
##############################################################################  
# configure shell  
##############################################################################  
  
RUN set -x \  
# .dotfiles  
&& git clone https://github.com/mkenney/.dotfiles.git /root/.dotfiles \  
&& chmod +rx /root \  
&& /root/.dotfiles/init.sh  
  
##############################################################################  
# vim plugin support  
##############################################################################  
  
RUN set -x \  
  
# YouCompleteMe support  
&& cd /root/.vim/bundle/YouCompleteMe \  
&& ./install.py \  
&& cd /root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/gocode \  
&& go build \  
&& cd
/root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/tern_runtime \  
&& npm install --production \  
  
# Cmd-T support  
&& cd /root/.vim/bundle/command-t/ruby/command-t \  
&& ruby extconf.rb \  
&& make  
  
##############################################################################  
# users  
##############################################################################  
  
RUN set -x \  
# Add a dev user  
&& groupadd dev \  
&& useradd dev -s /bin/bash -m -g dev -G root \  
&& echo "dev:password" | chpasswd \  
&& echo "dev ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers \  
  
# .dotfiles  
&& rsync -a /root/.dotfiles/ /home/dev/.dotfiles/ \  
&& chown -R dev:dev /home/dev/.dotfiles \  
&& sudo -u dev /home/dev/.dotfiles/init.sh  
  
##############################################################################  
# image resources  
##############################################################################  
  
COPY bin/devenv /usr/local/bin/devenv  
COPY _image /_image  
  
##############################################################################  
# SSH keys and mount scripts  
##############################################################################  
  
RUN set -x \  
# SSH keys used for communicating between containers  
&& cp -R /_image/network /home/dev/network \  
&& chown -R dev:dev /home/dev/network \  
&& cp -f /_image/network/sshd_config /etc/ssh/sshd_config \  
&& /etc/init.d/ssh start \  
# sshfs wrapper scripts  
&& cp -f /_image/network/mountenv /usr/local/bin \  
&& chmod 0755 /usr/local/bin/mountenv \  
&& cp -f /_image/network/umountenv /usr/local/bin \  
&& chmod 0755 /usr/local/bin/umountenv \  
&& chmod 777 /mnt  
  
##############################################################################  
# Oracle instantclient  
##############################################################################  
  
RUN set -x \  
&& groupadd dba -g 201 -o \  
&& useradd oracle -u 102 -o -s /bin/bash -m -g dba \  
&& echo "oracle:password" | chpasswd \  
&& cd /_image \  
&& dpkg -i oracle-
instantclient${ORACLE_VERSION_SHORT}-basic_${ORACLE_VERSION_LONG}_amd64.deb \  
&& dpkg -i oracle-
instantclient${ORACLE_VERSION_SHORT}-devel_${ORACLE_VERSION_LONG}_amd64.deb \  
&& dpkg -i oracle-
instantclient${ORACLE_VERSION_SHORT}-sqlplus_${ORACLE_VERSION_LONG}_amd64.deb
\  
&& mkdir -p /oracle/product \  
&& ln -s $ORACLE_HOME /oracle/product/latest \  
&& mkdir -p /oracle/product/latest/network/admin \  
  
# cleanup  
&& rm -f /oracle-
instantclient${ORACLE_VERSION_SHORT}-basic_${ORACLE_VERSION_LONG}_amd64.deb \  
&& rm -f /oracle-
instantclient${ORACLE_VERSION_SHORT}-devel_${ORACLE_VERSION_LONG}_amd64.deb \  
&& rm -f /oracle-
instantclient${ORACLE_VERSION_SHORT}-sqlplus_${ORACLE_VERSION_LONG}_amd64.deb  
  
##############################################################################  
# PHP  
##############################################################################  
  
# INI directory  
ENV PHP_INI_DIR /usr/local/etc/php/conf.d  
  
# server_env  
ENV server_env dev  
  
# Extensions and ini settings  
RUN set -x \  
# Packages  
# - libaio1 is required for oci8  
# - libicu-dev is required for intl  
# - libmemcached-dev is required for memcached  
# - libvpx-dev is required for GD  
# - libwebp-dev is required for GD  
# - libxpm-dev is required for GD  
# - libxml2-dev is required for soap  
# - php-pear is just good stuff  
&& apt-get install -qqy \  
libaio1 \  
libicu-dev \  
libpcre3-dev \  
libvpx-dev \  
libwebp-dev \  
libxpm-dev \  
libxml2-dev \  
php-pear  
  
RUN set -x \  
# Configure and install oci8  
# Don't poke it or it'll break  
&& cp /usr/include/oracle/${ORACLE_VERSION_SHORT}/client64/*
/oracle/product/latest/ \  
&& cd /oracle/product/latest \  
&& ln -s lib/libnnz11.so libnnz.so \  
&& ln -s lib/libnnz11.so libnnz11.so \  
&& ln -s lib/libclntsh.so.11.1 libclntsh.so \  
&& ln -s lib/libclntsh.so.11.1 libclntsh.so.11.1 \  
&& echo "instantclient,/oracle/product/latest" | pecl install oci8-2.1.1.tgz \  
&& echo "extension=oci8.so" > $PHP_INI_DIR/oci8.ini  
  
RUN set -x \  
# Extensions  
&& docker-php-source extract \  
&& docker-php-ext-configure gd \  
\--enable-gd-jis-conv \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-webp-dir=/usr/include/ \  
\--with-xpm-dir=/usr/include/ \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j$NPROC \  
gd \  
iconv \  
intl \  
mbstring \  
mcrypt \  
mysqli \  
pdo_mysql \  
pdo_pgsql \  
pcntl \  
soap \  
sockets \  
zip  
  
RUN set -x \  
# INI settings  
&& echo "memory_limit=-1" > $PHP_INI_DIR/memory_limit.ini \  
&& echo "date.timezone=${TIMEZONE}" > $PHP_INI_DIR/date_timezone.ini \  
&& echo "error_reporting=E_ALL" > $PHP_INI_DIR/error_reporting.ini \  
&& echo "display_errors=On" > $PHP_INI_DIR/display_errors.ini \  
&& echo "log_errors=On" > $PHP_INI_DIR/log_errors.ini \  
&& echo "report_memleaks=On" > $PHP_INI_DIR/report_memleaks.ini \  
&& echo "error_log=syslog" > $PHP_INI_DIR/error_log.ini  
  
##############################################################################  
# xdebug (for code-coverage reports)  
##############################################################################  
  
RUN set -x \  
&& yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.coverage_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.default_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
##############################################################################  
# composer  
##############################################################################  
  
RUN set -x \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& /usr/local/bin/composer config -g secure-http false  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
##############################################################################  
# codeception (includes phpunit)  
##############################################################################  
  
RUN set -x \  
&& composer global require "codeception/codeception:*"  
  
##############################################################################  
# phpDocumentor  
##############################################################################  
  
RUN set -x \  
&& apt-get -q -y install graphviz \  
&& pear channel-discover pear.phpdoc.org \  
&& pear install phpdoc/phpDocumentor  
  
##############################################################################  
# PHP linting  
##############################################################################  
  
COPY /_image/RpStandard /usr/local/phpcs/RpStandard  
COPY /_image/phpcs-ruleset.xml /usr/local/phpcs/phpcs-ruleset.xml  
COPY /_image/phpmd-ruleset.xml /usr/local/phpmd/phpmd-ruleset.xml  
COPY /_image/run-phpcs-checks /run-phpcs-checks  
COPY /_image/run-phpmd-checks /run-phpmd-checks  
COPY /_image/run-phpsyntax-checks /run-phpsyntax-checks  
  
RUN set -x \  
  
# CodeSniffer  
&& cd /usr/local/bin \  
&& curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& mkdir -p /usr/local/phpcs \  
  
# Mess Detector  
&& cd /usr/local/bin \  
&& curl -OL http://static.phpmd.org/php/latest/phpmd.phar \  
&& mkdir -p /usr/local/phpmd \  
  
&& chmod +x /usr/local/bin/php*.phar \  
  
# wrapper scripts  
&& chmod 0755 /run-phpcs-checks \  
&& chmod 0755 /run-phpmd-checks \  
&& chmod 0755 /run-phpsyntax-checks  
  
##############################################################################  
# kubectl  
##############################################################################  
  
RUN set -x \  
&& curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl \  
&& chmod +x ./kubectl \  
&& mv ./kubectl /usr/local/bin/kubectl  
  
##############################################################################  
# awscli  
##############################################################################  
  
RUN set -x \  
&& pip install --upgrade --user awscli \  
&& sudo -u dev pip install --upgrade --user awscli  
  
##############################################################################  
# terraform  
##############################################################################  
  
RUN set -x \  
&& curl -OL
https://releases.hashicorp.com/terraform/0.9.4/terraform_0.9.4_linux_amd64.zip
\  
&& unzip terraform_0.9.4_linux_amd64.zip \  
&& mv /terraform /usr/local/bin/terraform \  
&& chmod 0755 /usr/local/bin/terraform \  
&& rm -f terraform_0.9.4_linux_amd64.zip  
  
##############################################################################  
# configure environment  
##############################################################################  
  
RUN set -x \  
# env  
&& echo "set tags=/src/tags.devenv,./tags.devenv" | tee /root/.vimrc >>
/home/dev/.vimrc \  
&& echo "export ORACLE_HOME=$(echo $ORACLE_HOME)" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export LD_LIBRARY_PATH=$(echo $LD_LIBRARY_PATH)" | tee
/root/.bash_profile >> /home/dev/.bash_profile \  
&& echo "export TNS_ADMIN=$(echo $TNS_ADMIN)" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export CFLAGS=$(echo $CFLAGS)" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export NLS_LANG=$(echo $NLS_LANG)" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export LANG=$(echo $LANG)" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export LANGUAGE=$(echo $LANGUAGE)" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export LC_ALL=$(echo $LC_ALL)" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export TERM=xterm" | tee /root/.bash_profile >>
/home/dev/.bash_profile \  
&& echo "export PATH=$(echo $PATH)" | tee /root/.bash_profile >>
/home/dev/.bash_profile  
  
##############################################################################  
# terminal plugin support  
##############################################################################  
  
RUN set -x \  
# powerline config  
&& rsync -ac /_image/powerline/ /usr/share/powerline/ \  
&& mkdir -p /usr/local/powerline \  
&& ln -s /usr/share/powerline/bindings/tmux/powerline.conf
/usr/local/powerline/powerline.conf  
  
##############################################################################  
# postgresql support  
##############################################################################  
  
RUN set -x \  
# postgres client  
&& apt-get install -qqy postgresql-client  
  
##############################################################################  
# mysql / mariadb support  
##############################################################################  
  
RUN set -x \  
# mysql client  
&& apt-get install -qqy \  
mysql-client  
  
##############################################################################  
# ~ fin ~  
##############################################################################  
  
# generate the initial locate database  
# cleanup apt cache  
# add devenv support scripts  
# remove repo resources  
RUN set -x \  
&& updatedb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& cp /_image/attach.sh / \  
&& cp /_image/build-tags.sh / \  
&& cp /_image/init.sh / \  
&& rm -rf /_image  
  
USER dev  
VOLUME ["/src"]  
WORKDIR /src  
CMD ["/bin/bash"]  

