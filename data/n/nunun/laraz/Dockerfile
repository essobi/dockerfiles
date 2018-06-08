FROM nunun/alpine-nginx-php71:opcache  
  
# install packages from apk  
RUN apk upgrade -U \  
&& apk add --no-cache \  
bash git curl openssh outils-md5 \  
make g++ \  
python \  
mysql-client \  
nodejs nodejs-npm \  
php7-pdo_mysql php7-curl php7-session php7-phar \  
php7-tokenizer php7-xmlwriter php7-simplexml \  
tzdata  
  
# install groovy  
ENV GROOVY_HOME=/opt/groovy \  
GROOVY_VERSION=2.4.11 \  
JAVA_VERSION=8 \  
JAVA_UPDATE=131 \  
JAVA_BUILD=11 \  
JAVA_PATH=d54c1d3a095b4ff2b6607d096fa80163 \  
JAVA_HOME="/usr/lib/jvm/default-jvm"  
RUN echo "Installing Groovy Dependencies" \  
&& apk add --no-cache \  
ca-certificates gnupg openssl unzip \  
&& apk add --no-cache --virtual \  
.build-deps openjdk7-jre \  
&& echo "Downloading Groovy" \  
&& wget -O groovy.zip
"https://dist.apache.org/repos/dist/release/groovy/${GROOVY_VERSION}/distribution/apache-
groovy-binary-${GROOVY_VERSION}.zip" \  
&& echo "Importing keys listed in http://www.apache.org/dist/groovy/KEYS from
key server" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for key in "7FAA0F2206DE228F0DB01AD741321490758AAD6F" \  
"331224E1D7BE883D16E8A685825C06C827AF6B66" \  
"34441E504A937F43EB0DAEF96A65176A0FB1CD0B" \  
"9A810E3B766E089FFB27C70F11B595CEDC4AEBB5"; do \  
for server in ha.pool.sks-keyservers.net hkp://p80.pool.sks-keyservers.net:80
pgp.mit.edu; do \  
echo "Trying ${server}"; \  
if gpg --keyserver "${server}" \--recv-keys "${key}"; then break; fi; \  
done; \  
done \  
&& if [ $(gpg --list-keys | grep -c "pub ") -ne 4 ]; then \  
echo "ERROR: Failed to fetch GPG keys" >&2; exit 1; \  
fi \  
&& echo "Checking download signature" \  
&& wget -O groovy.zip.asc
"https://dist.apache.org/repos/dist/release/groovy/${GROOVY_VERSION}/distribution/apache-
groovy-binary-${GROOVY_VERSION}.zip.asc" \  
&& gpg --batch --verify groovy.zip.asc groovy.zip \  
&& rm -rf "${GNUPGHOME}" \  
&& rm groovy.zip.asc \  
&& echo "Installing Groovy" \  
&& unzip groovy.zip \  
&& rm groovy.zip \  
&& mkdir /opt \  
&& mv "groovy-${GROOVY_VERSION}" "${GROOVY_HOME}/" \  
&& ln -s "${GROOVY_HOME}/bin/grape" /usr/bin/grape \  
&& ln -s "${GROOVY_HOME}/bin/groovy" /usr/bin/groovy \  
&& ln -s "${GROOVY_HOME}/bin/groovyc" /usr/bin/groovyc \  
&& ln -s "${GROOVY_HOME}/bin/groovyConsole" /usr/bin/groovyConsole \  
&& ln -s "${GROOVY_HOME}/bin/groovydoc" /usr/bin/groovydoc \  
&& ln -s "${GROOVY_HOME}/bin/groovysh" /usr/bin/groovysh \  
&& ln -s "${GROOVY_HOME}/bin/java2groovy" /usr/bin/java2groovy \  
&& echo "Applying workaround for
https://issues.apache.org/jira/browse/GROOVY-7906" \  
&& sed -i "s|#!/bin/sh|#!/bin/bash|" "${GROOVY_HOME}/bin/grape" \  
&& sed -i "s|#!/bin/sh|#!/bin/bash|" "${GROOVY_HOME}/bin/groovy" \  
&& sed -i "s|#!/bin/sh|#!/bin/bash|" "${GROOVY_HOME}/bin/groovyc" \  
&& sed -i "s|#!/bin/sh|#!/bin/bash|" "${GROOVY_HOME}/bin/groovyConsole" \  
&& sed -i "s|#!/bin/sh|#!/bin/bash|" "${GROOVY_HOME}/bin/groovydoc" \  
&& sed -i "s|#!/bin/sh|#!/bin/bash|" "${GROOVY_HOME}/bin/groovysh" \  
&& sed -i "s|#!/bin/sh|#!/bin/bash|" "${GROOVY_HOME}/bin/java2groovy" \  
&& echo "Adding groovy user and group" \  
&& addgroup -S -g 1000 groovy \  
&& adduser -D -S -G groovy -u 1000 -s /bin/ash groovy \  
&& mkdir -p /home/groovy/.groovy/grapes \  
&& chown -R groovy:groovy /home/groovy  
  
# install groovy grape package swagger-codegen  
RUN grape install io.swagger swagger-codegen-cli 2.2.2  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# install phpunit  
RUN curl -sSL https://phar.phpunit.de/phpunit.phar -o phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
# configurations  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/supervisord.*.conf /etc/supervisor/conf.d/  
RUN rm -rf /var/www/html/*  
ADD src /var/www/html/  
WORKDIR /var/www/html/  
  
# start.sh  
ADD start.sh /  
CMD sh /start.sh  

