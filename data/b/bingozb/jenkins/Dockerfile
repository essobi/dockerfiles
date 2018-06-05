FROM jenkins/jenkins:alpine  
MAINTAINER bingo <bingov5@icloud.com>  
  
# Jenkins is using jenkins user, we need root to install things.  
USER root  
  
######################## Docker in Docker ########################  
  
RUN apk add --no-cache \  
ca-certificates  
  
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' >
/etc/nsswitch.conf  
  
ENV DOCKER_CHANNEL edge  
ENV DOCKER_VERSION 18.02.0-ce  
ENV DOCKER_HOST_ADDRESS "docker:2375"  
ENV DOCKER_HOST "tcp://$DOCKER_HOST_ADDRESS"  
  
RUN set -ex; \  
apk add --no-cache --virtual .fetch-deps \  
curl \  
tar \  
; \  
\  
apkArch="$(apk --print-arch)"; \  
case "$apkArch" in \  
x86_64) dockerArch='x86_64' ;; \  
armhf) dockerArch='armel' ;; \  
aarch64) dockerArch='aarch64' ;; \  
ppc64le) dockerArch='ppc64le' ;; \  
s390x) dockerArch='s390x' ;; \  
*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\  
esac; \  
\  
if ! curl -fL -o docker.tgz
"https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz";
then \  
echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from
'${DOCKER_CHANNEL}' for '${dockerArch}'"; \  
exit 1; \  
fi; \  
\  
tar --extract \  
\--file docker.tgz \  
\--strip-components 1 \  
\--directory /usr/local/bin/ \  
; \  
rm docker.tgz; \  
\  
apk del .fetch-deps; \  
\  
dockerd -v; \  
docker -v  
  
######################## Maven and Gradle ########################  
  
ENV MAVEN_VERSION 3.5.3  
ENV GRADLE_VERSION 4.6  
  
RUN apk add --no-cache --virtual .maven-gradle-deps wget curl tar unzip \  
&& mkdir /maven \  
&& curl
http://mirror.bit.edu.cn/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /maven --strip-components=1 \  
&& ln -s /maven/bin/mvn /usr/bin/mvn \  
&& wget -q https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
bin.zip \  
&& unzip -q gradle-$GRADLE_VERSION-bin.zip \  
&& rm -rf gradle-$GRADLE_VERSION-bin.zip \  
&& mv gradle-$GRADLE_VERSION gradle \  
&& ln -s /gradle/bin/gradle /usr/bin/gradle \  
&& apk del .maven-gradle-deps  
  
############################## PHP and Composer ##############################  
  
ENV PHPIZE_DEPS \  
autoconf \  
dpkg-dev dpkg \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c  
RUN apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
curl \  
tar \  
xz \  
openssl  
  
ENV PHP_VERSION 7.1.15  
ENV PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2"  
ENV PHP_CPPFLAGS="$PHP_CFLAGS"  
ENV PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie"  
ENV
PHP_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz/from/this/mirror"  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
RUN set -xe; \  
mkdir -p /usr/src; \  
cd /usr/src; \  
wget -O php.tar.xz "$PHP_URL"  
  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
coreutils \  
curl-dev \  
libedit-dev \  
openssl-dev \  
libxml2-dev \  
sqlite-dev \  
\  
&& export CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS" \  
&& mkdir -p /usr/src/php \  
&& tar -Jxf /usr/src/php.tar.xz -C /usr/src/php --strip-components=1 \  
&& cd /usr/src/php \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--disable-cgi \  
\--enable-ftp \  
\--enable-mbstring \  
\--enable-mysqlnd \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
\  
$(test "$gnuArch" = 's390x-linux-gnu' && echo '--without-pcre-jit') \  
\  
$PHP_EXTRA_CONFIGURE_ARGS \  
&& make -j "$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip
--strip-all '{}' \+ || true; } \  
&& ln -s /usr/local/bin/php /usr/bin/php \  
&& make clean \  
&& cd / \  
&& rm -rf /usr/src/php \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .php-rundeps $runDeps \  
\  
&& apk del .build-deps \  
\  
&& pecl update-channels \  
&& rm -rf /tmp/pear ~/.pearrc  
  
RUN apk add --no-cache --virtual .composer-deps curl \  
&& mkdir /php-composer \  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/php-
composer \  
&& ln -s /php-composer/composer.phar /usr/bin/composer \  
&& apk del .composer-deps  
  
########################## Node and Yarn #########################  
  
ENV NODE_VERSION 8.9.4  
ENV YARN_VERSION 1.3.2  
  
RUN apk add --no-cache \  
libstdc++ \  
&& apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
libgcc \  
linux-headers \  
make \  
python \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \  
&& tar -xf "node-v$NODE_VERSION.tar.xz" \  
&& cd "node-v$NODE_VERSION" \  
&& ./configure --without-npm \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& cd .. \  
&& rm -Rf "node-v$NODE_VERSION" \  
&& rm "node-v$NODE_VERSION.tar.xz"  
  
RUN apk add --no-cache --virtual .build-deps-yarn \  
curl \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz \  
&& apk del .build-deps-yarn  
  
########################## SSH config #########################  
  
RUN echo -e "\nHost *\n StrictHostKeyChecking no\n UserKnownHostsFile
/dev/null" >> /etc/ssh/ssh_config  
  
# Go back to jenkins user.  
USER jenkins  

