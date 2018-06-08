FROM repositoryjp/centos  
MAINTAINER Shinya Kinoshita <skinoshita@repositories.jp>  
  
LABEL name="PHP Environment Image" \  
description="The image for creating docker container of PHP environment." \  
distribution="centos" \  
centos-version="6.6" \  
phpbrew-version="1.20.6" \  
virtphp-version="0.5.2" \  
vendor="REPOSITORY <http://www.repositories.jp>" \  
license="MIT"  
  
USER root  
WORKDIR /tmp  
  
# Remove user named centos.  
RUN userdel -r centos  
  
# Create user named php.  
RUN groupadd php && useradd -s /bin/bash -g php php && passwd -d php  
RUN sed -i -e 's/AllowUsers centos/AllowUsers php/g' /etc/ssh/sshd_config  
  
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
php  
  
RUN ln -s /usr/lib64/libssl.so /usr/lib/libssl.so  
  
# Install virtphp  
RUN curl -L -O
https://github.com/virtphp/virtphp/releases/download/v0.5.2-alpha/virtphp.phar
&& \  
chmod a+x virtphp.phar && \  
mv virtphp.phar /usr/local/bin/virtphp  
  
# Install phpbrew.  
RUN wget https://github.com/phpbrew/phpbrew/archive/1.20.6.tar.gz && \  
tar xvzf 1.20.6.tar.gz && \  
cd phpbrew-1.20.6 && \  
chmod a+x phpbrew && \  
cp -p phpbrew /usr/local/bin/  
  
# Configure phpbrew.  
USER root  
WORKDIR /root  
  
RUN phpbrew init  
RUN echo "" >> ~/.bashrc  
RUN echo "# Source PHPbrew" >> ~/.bashrc  
RUN echo "export PHPBREW_SET_PROMPT=1" >> ~/.bashrc  
RUN echo "export PHPBREW_BIN=~/.phpbrew/bin" >> ~/.bashrc  
RUN echo "export PHPBREW_HOME=~/.phpbrew" >> ~/.bashrc  
RUN echo "export PHPBREW_ROOT=~/.phpbrew" >> ~/.bashrc  
RUN echo "[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc" >> ~/.bashrc  
  
USER php  
WORKDIR /home/php  
  
RUN phpbrew init  
RUN echo "" >> ~/.bashrc  
RUN echo "# Source PHPbrew" >> ~/.bashrc  
RUN echo "export PHPBREW_SET_PROMPT=1" >> ~/.bashrc  
RUN echo "export PHPBREW_BIN=~/.phpbrew/bin" >> ~/.bashrc  
RUN echo "export PHPBREW_HOME=~/.phpbrew" >> ~/.bashrc  
RUN echo "export PHPBREW_ROOT=~/.phpbrew" >> ~/.bashrc  
RUN echo "[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc" >> ~/.bashrc  
  
# Configure container.  
USER root  
WORKDIR /root  
  
ENTRYPOINT ["/bin/bash", "-c"]  
CMD ["/etc/init.d/sshd start && /bin/bash"]  

