FROM ubuntu:16.04  
ENV LANG C.UTF-8  
ENV RUBY_INSTALL_VERSION 0.6.1  
ENV RUBY_VERSION 2.4  
RUN apt-get update && apt-get install -y --no-install-recommends \  
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
RUN passenger-install-nginx-module  
RUN sed -i \  
-e "s/root html;/passenger_enabled on;/" \  
-e "s/index index.html index.htm;/root \/srv\/rails\/app\/public;/" \  
/opt/nginx/conf/nginx.conf &&\  
echo "daemon off;" >> /opt/nginx/conf/nginx.conf  
RUN rm -fr /opt/nginx/logs  
RUN mkdir /var/log/nginx  
RUN ln -s /var/log/nginx /opt/nginx/logs  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config /config  
COPY run.sh /run.sh  
  
RUN chmod 755 /run.sh  
  
CMD ["/run.sh"]  
  

