FROM repositoryjp/centos:6.6  
MAINTAINER Shinya Kinoshita <skinoshita@repositories.jp>  
  
LABEL name="virtPHP Image" \  
description="The image for creating docker container of virtPHP 0.5.2." \  
distribution="centos" \  
centos-version="6.6" \  
phpbrew-version="1.21.3" \  
virtphp-version="0.5.2" \  
vendor="REPOSITORY <http://www.repositories.jp>" \  
license="MIT"  
  
USER root  
WORKDIR /tmp  
  
# Install necessary packages.  
RUN yum install -y readline-devel \  
libxml2 \  
libxml2-devel \  
libxslt-devel \  
openssl-devel \  
libmcrypt \  
libmcrypt-devel \  
postgresql-devel \  
libicu \  
libicu-devel \  
libmcrypt \  
libmcrypt-devel \  
lcov \  
gmp-devel \  
libcurl-devel \  
libtidy \  
libtidy-devel \  
libpng \  
libpng-devel \  
libjpeg \  
libjpeg-devel \  
php  
  
# create symbolic link for libssl.  
RUN ln -s /usr/lib64/libssl.so /usr/lib/libssl.so  
  
# Install phpbrew.  
RUN wget https://github.com/phpbrew/phpbrew/archive/1.21.3.tar.gz && \  
tar xvzf 1.21.3.tar.gz && \  
cd phpbrew-1.21.3 && \  
chmod a+x phpbrew && \  
cp -p phpbrew /usr/local/bin/  
  
# Configure phpbrew.  
RUN phpbrew init  
RUN echo "" >> ~/.bashrc  
RUN echo "# Source PHPbrew" >> ~/.bashrc  
RUN echo "export PHPBREW_SET_PROMPT=1" >> ~/.bashrc  
RUN echo "export PHPBREW_BIN=~/.phpbrew/bin" >> ~/.bashrc  
RUN echo "export PHPBREW_HOME=~/.phpbrew" >> ~/.bashrc  
RUN echo "export PHPBREW_ROOT=~/.phpbrew" >> ~/.bashrc  
RUN echo "[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc" >> ~/.bashrc  
  
# Install virtphp  
RUN curl -L -O
https://github.com/virtphp/virtphp/releases/download/v0.5.2-alpha/virtphp.phar
&& \  
chmod a+x virtphp.phar && \  
mv virtphp.phar /usr/local/bin/virtphp  
  
# Configure container.  
USER root  
WORKDIR /root  
  
CMD ["/usr/sbin/sshd", "-D"]  

