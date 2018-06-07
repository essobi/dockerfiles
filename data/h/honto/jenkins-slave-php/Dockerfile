FROM php:7.0-cli  
MAINTAINER takakazu.kaneko<ztakakazu.kaneko@2dfacto.co.jp>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y unzip openssh-server sudo zlib1g-dev  
  
# Install Git  
RUN apt-get install -y gcc \  
make \  
autoconf \  
libcurl4-gnutls-dev \  
libexpat1-dev \  
gettext \  
libz-dev \  
libssl-dev \  
git \  
expect  
RUN git clone -b v2.6.3 https://github.com/git/git.git /usr/local/src/git  
RUN apt-get remove -y git  
  
WORKDIR /usr/local/src/git  
RUN make configure && \  
./configure --prefix=/usr/local && \  
make && \  
make install  
WORKDIR /var/jenkins_home  
  
RUN rm -rf /usr/local/src/git  
  
# Install JDK  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
ENV JAVA_VERSION 8u66  
ENV JAVA_DEBIAN_VERSION 8u66-b17-1~bpo8+1  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20140324  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION"  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-
amd64/jre/bin/java  
  
# Setup Jenkins  
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
RUN adduser jenkins  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Setup PHP  
RUN docker-php-ext-install zip mbstring pdo_mysql mysqli && \  
curl -L -O https://www.phing.info/get/phing-latest.phar && \  
chmod 755 phing-latest.phar && \  
mv phing-latest.phar /usr/local/bin/phing && \  
curl -L -O https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && \  
chmod 755 phpcs.phar && \  
mv phpcs.phar /usr/local/bin/phpcs && \  
curl -L -O http://static.phpmd.org/php/latest/phpmd.phar && \  
chmod 755 phpmd.phar && \  
mv phpmd.phar /usr/local/bin/phpmd && \  
curl -L -O https://phar.phpunit.de/phpcpd.phar && \  
chmod 755 phpcpd.phar && \  
mv phpcpd.phar /usr/local/bin/phpcpd && \  
curl -L -O http://phpdoc.org/phpDocumentor.phar && \  
chmod 755 phpDocumentor.phar && \  
mv phpDocumentor.phar /usr/local/bin/phpdoc && \  
curl -L -O https://phar.phpunit.de/phpunit.phar && \  
chmod 755 phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit && \  
curl -L -O https://getcomposer.org/composer.phar && \  
chmod 755 composer.phar && \  
mv composer.phar /usr/local/bin/composer  
  
RUN curl -L -O http://xdebug.org/files/xdebug-2.4.0rc3.tgz && \  
tar zxfv xdebug-2.4.0rc3.tgz && \  
cd xdebug-2.4.0RC3/ && \  
phpize && \  
./configure --enable-xdebug && \  
make && \  
make install  
  
# Cleanup  
RUN rm -rf /var/lib/apt/lists/*  
  
# Finalize  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

