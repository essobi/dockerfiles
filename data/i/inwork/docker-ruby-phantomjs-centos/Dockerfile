FROM centos:7  
ENV RUBY_VERSION 2.3.1  
ENV PHANTOMJS_VERSION 2.1.1  
# URL and SHA256 for ruby  
ENV RUBY_DOWNLOAD_URL http://cache.ruby-
lang.org/pub/ruby/ruby-$RUBY_VERSION.tar.gz  
ENV RUBY_DOWNLOAD_SHA256
b87c738cb2032bf4920fef8e3864dc5cf8eae9d89d8d523ce0236945c5797dcd  
  
# find URL and SHA256 on http://phantomjs.org/download.html  
ENV PHANTOMJS_DOWNLOAD_URL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2  
ENV PHANTOMJS_DOWNLOAD_SHA256
86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f  
  
# install general pre-requisites  
RUN yum install -y epel-release  
RUN yum install -y tar bzip2 git sqlite-devel make gcc gcc-c++ ruby-devel
zlib-devel postgresql-devel cmake openssh-client libxml2-devel libxslt-devel
nodejs npm autoconf  
  
# installing webkit - useful for CI webapps  
RUN yum install -y qtwebkit-devel  
RUN ln -s /usr/lib64/qt4/bin/qmake /usr/bin/qmake  
  
# INSTALL RUBY & rubygems  
RUN set -ex \  
&& curl -fSL -o ruby.tar.gz "$RUBY_DOWNLOAD_URL" \  
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
&& rm -r /usr/src/ruby  
  
RUN gem install bundler rspec rails  
  
# INSTALL PHANTOMJS  
RUN yum install -y fontconfig freetype freetype-devel fontconfig-devel
libstdc++  
  
RUN mkdir -p /opt/phantomjs/  
RUN curl -fsSL "$PHANTOMJS_DOWNLOAD_URL" -o phantomjs.tar.bz2  
RUN echo "$PHANTOMJS_DOWNLOAD_SHA256 phantomjs.tar.bz2" | sha256sum -c -  
RUN tar -xvf phantomjs.tar.bz2 -C /opt/phantomjs  
RUN rm phantomjs.tar.bz2  
  
ENV PATH $PATH:/opt/phantomjs/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/  

