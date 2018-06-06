# See https://github.com/docker-
library/php/blob/4677ca134fe48d20c820a19becb99198824d78e3/7.0/fpm/Dockerfile  
FROM php:7.2-fpm  
  
MAINTAINER Daniel Brooks <dbrooks@dabsquared.com>  
  
  
# A few reasons for installing distribution-provided OpenJDK:  
#  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
#  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
#  
# For some sample build times, see Debian's buildd logs:  
# https://buildd.debian.org/status/logs.php?pkg=openjdk-8  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
git \  
openssh-client \  
ssh-askpass \  
gnupg \  
dirmngr \  
procps \  
  
&& rm -rf /var/lib/apt/lists/*  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe  
RUN ln -svT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)"
/docker-java-home  
ENV JAVA_HOME /docker-java-home  
  
ENV JAVA_VERSION 8u151  
ENV JAVA_DEBIAN_VERSION 8u151-b12-1~deb9u1  
  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20170531+nmu1  
  
RUN set -ex; \  
\  
# deal with slim variants not having man page directories (which causes
"update-alternatives" to fail)  
if [ ! -d /usr/share/man/man1 ]; then \  
mkdir -p /usr/share/man/man1; \  
fi; \  
\  
apt-get update; \  
apt-get install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
# verify that "docker-java-home" returns what we expect  
[ "$(readlink -f "$JAVA_HOME")" = "$(docker-java-home)" ]; \  
\  
# update-alternatives so that future installs of other OpenJDK versions don't
change /usr/bin/java  
update-alternatives --get-selections | awk -v home="$(readlink -f
"$JAVA_HOME")" 'index($3, home) == 1 { $2 = "manual"; print | "update-
alternatives --set-selections" }'; \  
# ... and verify that it actually worked for one of the alternatives we care
about  
update-alternatives --query java | grep -q 'Status: manual'  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
######Node  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \  
gpg --keyserver hkp://keyserver.pgp.com:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" ; \  
done  
  
ENV NODE_VERSION 9.8.0  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
i386) ARCH='x86';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 --no-same-owner \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV YARN_VERSION 1.5.1  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" || \  
gpg --keyserver hkp://keyserver.pgp.com:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
#######Ruby  
RUN apt-get update && apt-get install -y libssl-dev libreadline-dev zlib1g-dev  
  
RUN git clone git://github.com/rbenv/rbenv.git /usr/local/rbenv \  
&& git clone git://github.com/rbenv/ruby-build.git
/usr/local/rbenv/plugins/ruby-build \  
&& git clone git://github.com/jf/rbenv-gemset.git
/usr/local/rbenv/plugins/rbenv-gemset \  
&& /usr/local/rbenv/plugins/ruby-build/install.sh  
ENV PATH /usr/local/rbenv/bin:$PATH  
ENV RBENV_ROOT /usr/local/rbenv  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh \  
&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /root/.bashrc \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /root/.bashrc \  
&& echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
  
ENV CONFIGURE_OPTS --disable-install-doc  
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH  
  
RUN rbenv init - && rbenv install 2.4.1  
RUN rbenv init - && rbenv global 2.4.1  
RUN rbenv init - && gem update --system  
RUN rbenv init - && gem install bundler --force  
  
####Our actual php stuff  
COPY php.ini /usr/local/etc/php/  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip \  
bzip2 \  
libbz2-dev \  
libsodium-dev \  
libpng-dev \  
libjpeg-dev \  
libxml2-dev \  
libwebp-dev \  
libxslt-dev \  
libicu-dev \  
libssh2-1 \  
libssh2-1-dev \  
libmcrypt-dev \  
libfreetype6-dev \  
curl \  
libcurl4-gnutls-dev \  
pdftk \  
graphviz \  
acl \  
libfcgi0ldbl  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# Set timezone  
ENV TZ=Etc/GMT+7  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN date  
  
# Type docker-php-ext-install to see available extensions  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install pdo pdo_mysql bcmath bz2 gd xml xsl json intl soap
curl mbstring zip calendar pcntl shmop exif opcache  
  
RUN pecl install apcu-beta  
RUN docker-php-ext-enable --ini-name=20-apcu.ini apcu  
  
RUN pecl install apcu_bc-1.0.3  
RUN docker-php-ext-enable --ini-name=21-apc.ini apc  
  
RUN pecl install ssh2-1.0  
RUN docker-php-ext-enable ssh2  
  
RUN pecl install redis  
RUN docker-php-ext-enable redis  
  
RUN pecl install mcrypt-1.0.1  
RUN docker-php-ext-enable mcrypt  
  
## # install xdebug  
#RUN pecl install xdebug  
#RUN docker-php-ext-enable xdebug  
#RUN echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
#RUN echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
#RUN echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
#RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
#RUN echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
#RUN echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
#RUN echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
#RUN mv /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
/usr/local/etc/php/docker-php-ext-xdebug.ini  
RUN echo 'alias sf3="php bin/console"' >> ~/.bashrc  
RUN echo '{ "allow_root": true }' > ~/.bowerrc  
  
ENV ISDEV=false  
ENV ENVIRONMENT="prod"  
ENV DB_DIR=".data/db/"  
COPY setup.sh /setup.sh  
RUN chmod +x /setup.sh  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
WORKDIR "/var/www/symfony"  
  
EXPOSE 9000  
CMD ["php-fpm"]  
  
HEALTHCHECK \--interval=320s --timeout=10s --retries=10 \  
CMD \  
SCRIPT_NAME=/app.php \  
SCRIPT_FILENAME=/app.php \  
REQUEST_METHOD=GET \  
cgi-fcgi -bind -connect 127.0.0.1:9000 || exit 1  

