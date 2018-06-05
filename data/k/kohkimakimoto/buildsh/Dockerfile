FROM centos:centos7  
  
# docker yum repo  
# https://docs.docker.com/engine/installation/linux/centos/  
RUN echo $'[dockerrepo]\n\  
name=Docker Repository\n\  
baseurl=https://yum.dockerproject.org/repo/main/centos/7/\n\  
enabled=1\n\  
gpgcheck=1\n\  
gpgkey=https://yum.dockerproject.org/gpg' > /etc/yum.repos.d/docker.repo  
  
# deps  
RUN yum -y install \  
epel-release \  
http://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm \  
&& yum clean all && \  
yum -y install \  
git \  
man-db \  
curl \  
wget \  
gcc \  
gcc-c++ \  
make \  
gettext \  
unzip \  
tar \  
vim-enhanced \  
sudo \  
tree \  
patch \  
zlib \  
zlib-devel \  
bzip2 \  
bzip2-devel \  
readline \  
readline-devel \  
sqlite \  
sqlite-devel \  
libxml2 \  
libxml2-devel \  
libicu-devel \  
libcurl \  
libcurl-devel \  
libjpeg \  
libjpeg-devel \  
libpng \  
libpng-devel \  
freetype \  
freetype-devel \  
libmcrypt \  
libmcrypt-devel \  
libtidy \  
libtidy-devel \  
libxslt \  
libxslt-devel \  
file \  
file-devel \  
bison \  
bison-devel \  
re2c \  
openssl \  
openssl-devel \  
autoconf \  
automake \  
libtool \  
mysql-community-client \  
docker-engine \  
&& mkdir -p /build \  
&& chmod -R 777 "/build"  
  
# Python  
ENV PYTHON_VERSION 3.6.3  
RUN git clone https://github.com/yyuu/pyenv.git /opt/pyenv  
ENV PYENV_ROOT /opt/pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  
RUN pyenv install ${PYTHON_VERSION} && pyenv global ${PYTHON_VERSION} && pyenv
rehash  
  
# Node.js  
ENV NODE_VERSION v8.9.2  
RUN git clone https://github.com/riywo/ndenv /opt/ndenv \  
&& git clone https://github.com/riywo/node-build.git /opt/ndenv/plugins/node-
build  
ENV NDENV_ROOT /opt/ndenv  
ENV PATH $NDENV_ROOT/shims:$NDENV_ROOT/bin:$PATH  
RUN ndenv install ${NODE_VERSION} && ndenv global ${NODE_VERSION} && ndenv
rehash  
# yarn https://yarnpkg.com  
RUN cd /opt \  
&& wget
https://github.com/yarnpkg/yarn/releases/download/v1.3.2/yarn-v1.3.2.tar.gz \  
&& tar zvxf yarn-v1.3.2.tar.gz \  
&& mv yarn-v1.3.2 yarn  
ENV PATH /opt/yarn/bin:$PATH  
  
# PHP  
ENV PHP_VERSION 7.1.9  
RUN git clone https://github.com/madumlao/phpenv.git /opt/phpenv \  
&& git clone https://github.com/php-build/php-build.git
/opt/phpenv/plugins/php-build  
ENV PHPENV_ROOT /opt/phpenv  
ENV PATH $PHPENV_ROOT/shims:$PHPENV_ROOT/bin:$PATH  
RUN phpenv install ${PHP_VERSION} && phpenv global ${PHP_VERSION} && phpenv
rehash  
# composer  
RUN curl -L https://getcomposer.org/composer.phar -o /usr/bin/composer &&
chmod 755 /usr/bin/composer  
  
# Ruby  
ENV RUBY_VERSION 2.3.4  
RUN git clone https://github.com/rbenv/rbenv.git /opt/rbenv \  
&& git clone https://github.com/rbenv/ruby-build.git /opt/rbenv/plugins/ruby-
build  
ENV RBENV_ROOT /opt/rbenv  
ENV PATH $RBENV_ROOT/shims:$RBENV_ROOT/bin:$PATH  
RUN rbenv install ${RUBY_VERSION} && rbenv global ${RUBY_VERSION} && rbenv
rehash  
# bundler  
RUN gem install bundler  
  
# Perl  
ENV PERL_VERSION 5.25.10  
RUN git clone https://github.com/tokuhirom/plenv.git /opt/plenv \  
&& git clone https://github.com/tokuhirom/Perl-Build.git
/opt/plenv/plugins/perl-build  
ENV PLENV_ROOT /opt/plenv  
ENV PATH $PLENV_ROOT/shims:$PLENV_ROOT/bin:$PATH  
RUN plenv install ${PERL_VERSION} && plenv global ${PERL_VERSION} && plenv
rehash  
  
# Go  
ENV GOVERSION 1.9.2  
ADD https://storage.googleapis.com/golang/go${GOVERSION}.linux-amd64.tar.gz
/tmp/go${GOVERSION}.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf /tmp/go${GOVERSION}.linux-amd64.tar.gz \  
&& rm /tmp/go${GOVERSION}.linux-amd64.tar.gz  
ENV GOPATH /build  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
# sudo config  
RUN sed -i -e 's/Defaults[ ]*env_reset/#Defaults env_reset/' /etc/sudoers \  
&& sed -i -e 's/Defaults[ ]*secure_path/#Defaults secure_path/' /etc/sudoers \  
&& echo 'Defaults env_keep += "PATH"' >> /etc/sudoers  
  
# misc  
# wait-for-it  
RUN git clone https://github.com/vishnubob/wait-for-it.git /opt/wait-for-it \  
&& ln -s /opt/wait-for-it/wait-for-it.sh /usr/bin/wait-for-it.sh  
  
WORKDIR /build  
CMD ["/bin/bash"]  

