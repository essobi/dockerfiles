#  
# Cartodb container  
#  
FROM ubuntu:14.04  
# Configuring locales  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-reconfigure locales && locale-gen en_US.UTF-8 && update-locale
LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update  
RUN apt-get install -y -q \  
build-essential \  
ca-certificates \  
imagemagick \  
autoconf \  
automake \  
libtool \  
checkinstall \  
unp \  
zip \  
unzip \  
git-core \  
git \  
curl \  
openssl \  
libreadline6 \  
zlib1g \  
zlib1g-dev \  
libssl-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
libxml2-dev \  
libxslt-dev \  
libc6-dev \  
postgresql-9.3 \  
postgresql-client-9.3 \  
\--no-install-recommends  
  
RUN git config --global user.email spocksplanet@gmail.com  
RUN git config --global user.name "Volkan Unsal"  
  
# Install rvm  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 && \  
curl -L https://get.rvm.io | bash -s stable --ruby && \  
echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc && \  
/bin/bash -l -c rvm requirements && \  
echo rvm_max_time_flag=15 >> ~/.rvmrc && \  
/bin/bash -l -c 'rvm install 2.2.3' && \  
/bin/bash -l -c 'rvm use 2.2.3 --default' && \  
/bin/bash -l -c 'gem install bundle archive-tar-minitar'  
  
# Install CartoDB  
RUN git clone git://github.com/CartoDB/cartodb.git  
WORKDIR cartodb  
RUN git reset --hard 59c286b04363e983d346b80ba113dcd63de0a83c  
  
RUN apt-get install -y -q postgresql-server-dev-9.3  
  
RUN /bin/bash -l -c "gem install pg -v '0.15.0'"  
  
RUN apt-get install -y -q postgresql-server-dev-9.3 \  
libicu-dev  
  
RUN /bin/bash -l -c 'bundle install'  
  
# Install bundler  
RUN /bin/bash -l -c 'gem install bundler --no-doc --no-ri'  
  
# Configurations  
ADD ./config/app_config.yml /cartodb/config/app_config.yml  
ADD ./config/database.yml /cartodb/config/database.yml  
ADD ./script/create_dev_user /cartodb/script/create_dev_user  
ADD ./script/setup_organization /cartodb/script/setup_organization  
RUN mkdir -p /cartodb/log && touch /cartodb/log/users_modifications  
  
# Finish  
ADD ./startup.sh /opt/startup.sh  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/bin/bash", "/opt/startup.sh"]  
  
# Install NodeJS  
RUN curl
https://nodejs.org/download/release/v0.10.41/node-v0.10.41-linux-x64.tar.gz|
tar -zxf - --strip-components=1 -C /usr  
  
ENV PORT 8080  
# HACK  
ADD ./config/db_service.rb /cartodb/app/models/user/db_service.rb  
  
# Clean up  
RUN rm -rf /var/lib/apt/lists/*

