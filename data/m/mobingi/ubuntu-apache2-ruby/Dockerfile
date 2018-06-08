FROM ubuntu:16.04  
LABEL maintainer="mobingi,Inc."  
  
ENV LANG C.UTF-8  
ENV RUBY_INSTALL_VERSION 0.6.1  
ENV RUBY_VERSION 2.3  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apache2 \  
apache2-dev \  
bison \  
build-essential \  
ca-certificates \  
git \  
libapr1-dev \  
libaprutil1-dev \  
libcurl4-openssl-dev \  
libffi-dev \  
libgdbm-dev \  
libmysqlclient-dev \  
libpq-dev \  
libncurses5-dev \  
libreadline-dev \  
libsqlite3-dev \  
libyaml-dev \  
make \  
nodejs \  
supervisor \  
tzdata \  
wget \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -fr /var/lib/apt/lists/*  
  
RUN wget -O ruby-install-$RUBY_INSTALL_VERSION.tar.gz
https://github.com/postmodern/ruby-
install/archive/v$RUBY_INSTALL_VERSION.tar.gz \  
&& tar -zxf ruby-install-$RUBY_INSTALL_VERSION.tar.gz  
  
WORKDIR /ruby-install-$RUBY_INSTALL_VERSION  
RUN make install  
  
WORKDIR /  
RUN ruby-install --system ruby $RUBY_VERSION \-- --disable-install-rdoc  
RUN gem update --system  
RUN gem install passenger --no-ri --no-rdoc  
RUN passenger-install-apache2-module  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config /config  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
COPY run.sh /run.sh  
  
RUN chmod 755 /run.sh  
  
CMD ["/run.sh"]  

