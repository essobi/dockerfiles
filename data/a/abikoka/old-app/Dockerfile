FROM centos:6  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN rpm -ivh http://repo.okay.com.mx/centos/6/x86_64/release/okay-
release-1-1.noarch.rpm  
  
RUN set -xe && \  
yum update -y && yum install -y \  
bzip2 \  
curl \  
db4-devel \  
gcc \  
gcc-c++ \  
git \  
gdbm-devel \  
gd-last \  
gtk3 \  
gtk3-devel \  
httpd \  
httpd-tools \  
ImageMagick \  
ImageMagick-devel \  
java-1.8.0-openjdk \  
openssl \  
openssl-devel \  
readline-devel \  
s3cmd \  
sudo \  
tcl-devel \  
libmcrypt \  
libyaml-devel \  
mod_ssl \  
nkf \  
unzip \  
vim \  
wget \  
xorg-x11-server-Xvfb \  
xwd \  
netpbm-progs \  
xz \  
yum-utils && \  
yum install -y --enablerepo=remi \  
php \  
php-mbstring \  
php-pear \  
php-devel \  
php-gd \  
php-pdo \  
php-mysql \  
php-mcrypt \  
php-xml \  
php-opcache \  
&& yum groupinstall -y "X Window System" \  
&& yum groupinstall -y "Japanese Support" \  
&& package-cleanup --dupes \  
&& package-cleanup --cleandupes \  
&& yum clean all  
  
RUN fc-cache -fv  
  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
COPY php.conf /etc/httpd/conf.d/php.conf  
COPY ssl.conf /etc/httpd/conf.d/ssl.conf  
COPY php.ini /etc/php.ini  
  
# Install Composer  
RUN pear config-set php_ini /etc/php.ini  
RUN pecl config-set php_ini /etc/php.ini  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& composer config -g repositories.packagist composer https://packagist.jp \  
&& pecl install mongo json imagick apc \  
&& pecl install redis-2.2.8 \  
&& pear channel-discover pear.bovigo.org \  
&& pear install bovigo/vfsStream-beta  
  
RUN chkconfig httpd on  
  
ENV RUBY_MAJOR 1.9  
ENV RUBY_VERSION 1.9.3-p551  
ENV RUBY_DOWNLOAD_SHA256
bb5be55cd1f49c95bb05b6f587701376b53d310eb1bb7c76fbd445a1c75b51e8  
# ENV RUBY_MAJOR 2.2  
# ENV RUBY_VERSION 2.2.2  
# ENV RUBY_DOWNLOAD_SHA256
5ffc0f317e429e6b29d4a98ac521c3ce65481bfd22a8cf845fa02a7b113d9b44  
ENV RUBYGEMS_VERSION 2.6.4  
ENV NODE_VERSION 0.10.45  
# skip installing gem documentation  
RUN mkdir -p /usr/local/etc \  
&& { \  
echo 'install: --no-document'; \  
echo 'update: --no-document'; \  
} >> /usr/local/etc/gemrc  
  
# some of ruby's build scripts are written in ruby  
# we purge this later to make sure our final image uses what we just built  
RUN set -ex \  
&& curl -fSL -o ruby.tar.gz "http://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz" \  
&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/ruby \  
&& tar -xzf ruby.tar.gz -C /usr/src/ruby --strip-components=1 \  
&& rm ruby.tar.gz \  
&& cd /usr/src/ruby \  
&& { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new &&
mv file.c.new file.c \  
&& autoconf \  
&& ./configure --disable-install-doc \  
&& make -j"$(nproc)" \  
&& make install \  
&& make clean \  
&& gem update --system $RUBYGEMS_VERSION \  
&& rm -r /usr/src/ruby  
  
ENV BUNDLER_VERSION 1.12.5  
RUN gem install bundler --version "$BUNDLER_VERSION"  
  
# install things globally, for great justice  
# and don't create ".bundle" in all our apps  
ENV GEM_HOME /usr/local/bundle  
ENV BUNDLE_PATH="$GEM_HOME" \  
BUNDLE_BIN="$GEM_HOME/bin" \  
BUNDLE_SILENCE_ROOT_WARNING=1 \  
BUNDLE_APP_CONFIG="$GEM_HOME"  
ENV PATH $BUNDLE_BIN:$PATH  
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \  
&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"  
  
# node  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& npm install -g less@1.3.0 phantomjs  
  
# firefox-17  
RUN curl -SLO "https://download-
installer.cdn.mozilla.net/pub/firefox/releases/17.0.9esr/linux-x86_64/ja/firefox-17.0.9esr.tar.bz2"  
RUN tar jxvf "firefox-17.0.9esr.tar.bz2"  
# RUN curl -SLO
"https://ftp.mozilla.org/pub/firefox/releases/45.2.0esr/linux-x86_64/ja/firefox-45.2.0esr.tar.bz2"  
# RUN tar jxvf "firefox-45.2.0esr.tar.bz2"  
RUN ln -s /firefox/firefox /usr/bin/firefox  
RUN chmod a+x /usr/bin/firefox  
  
RUN chmod -R 755 /usr/local/bin  
RUN chmod -R 755 /var/www  
WORKDIR /var/www  
  
ENV PATH $PATH:/var/www/bin  
RUN echo $PATH  
  
EXPOSE 80  
# EXPOSE 443  
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]

