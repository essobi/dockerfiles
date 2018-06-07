# FROM ruby:2.3.0  
FROM ubuntu:latest  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends mysql-server tcl && \  
apt-get install --no-install-recommends -y -q curl python build-essential git
ca-certificates && \  
apt-get install -y libgmp3-dev && \  
apt-get clean  
  
RUN { \  
echo '[mysqld]'; \  
echo 'character-set-server=utf8'; \  
echo 'collation-server=utf8_general_ci'; \  
echo '[client]'; \  
echo 'default-character-set=utf8'; \  
} > /etc/mysql/conf.d/charset.cnf  
  
ENV REDIS_VERSION 3.2.4  
RUN cd /tmp && \  
wget http://download.redis.io/releases/redis-$REDIS_VERSION.tar.gz && \  
tar xfvz redis-$REDIS_VERSION.tar.gz && \  
cd redis-$REDIS_VERSION && \  
make && \  
make install && \  
cd ../ && \  
rm -f redis-$REDIS_VERSION.tar.gz && \  
rm -rf redis-$REDIS_VERSION  
  
RUN mkdir /nodejs && \  
curl http://nodejs.org/dist/v0.10.30/node-v0.10.30-linux-x64.tar.gz | tar xvzf
- -C /nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
  
# FROM sivapraveen/ruby23-mysql-redis-nodejs:v1  
# ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
# # RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
# # && unset GEM_HOME \  
# # && \curl -sSL https://get.rvm.io | bash -s stable --ruby \  
# # && /bin/bash -l -c "source /usr/local/rvm/scripts/rvm"  
# # RUN /bin/bash -l -c "rvm install 2.1" \  
# # && /bin/bash -l -c "rvm install 2.2" \  
# # && /bin/bash -l -c "rvm install 2.3.0" \  
# # && /bin/bash -l -c "rvm install 2.3.1" \  
# # && /bin/bash -l -c "rvm install 2.3.2" \  
# # && /bin/bash -l -c "rvm install 2.3.3" \  
# # && /bin/bash -l -c "rvm install 2.4.0" \  
# # && /bin/bash -l -c "rvm --default 2.4.0" \  
# # && /bin/bash -l -c "rvm list"  
# MAINTAINER NoSkillGuy <rsivapraveen001@gmail.com>  
# #Install rvm  
# RUN apt-get update -qq  
# RUN apt-get install -y --no-install-recommends ca-certificates wget  
# RUN wget -O /usr/local/bin/rvm-installer
"https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-installer"  
# RUN wget -O /usr/local/bin/rvm-installer.asc
"https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-
installer.asc"  
# RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
# RUN gpg --batch --verify /usr/local/bin/rvm-installer.asc
/usr/local/bin/rvm-installer  
# RUN rm -r /usr/local/bin/rvm-installer.asc  
# RUN chmod +x /usr/local/bin/rvm-installer  
# RUN /bin/bash rvm-installer stable  
# RUN . /etc/profile.d/rvm.sh  
# RUN rvm requirements  
# RUN rvm install ruby-2.3  
# RUN rvm install 2.1  
# RUN rvm install 2.2  
# RUN rvm install 2.3.0  
# RUN rvm install 2.3.1  
# RUN rvm install 2.3.2  
# RUN rvm install 2.3.3  
# RUN rvm install 2.4.0  
# RUN rvm list  
# RUN echo "source /usr/local/rvm/scripts/rvm" >> /etc/profile  
# RUN echo "rvm use ruby-2.4.0 --default" >> /etc/profile  
# CMD [/bin/bash", "-l"]  
RUN apt-get update -qqy && apt-get install -qqy \  
bzip2 \  
gawk \  
g++ \  
gcc \  
make \  
libreadline6-dev \  
libyaml-dev \  
libsqlite3-dev \  
sqlite3 \  
autoconf \  
libgmp-dev \  
libgdbm-dev \  
libncurses5-dev \  
automake \  
libtool \  
bison \  
pkg-config \  
libffi-dev \  
&& rm -rf /var/lib/apt/lists  
  
# additional packages for development  
RUN apt-get update -qqy && apt-get install -qqy \  
git \  
curl \  
nodejs \  
libpq-dev \  
libmysqlclient-dev \  
qt5-default \  
libqt5webkit5-dev \  
imagemagick \  
libmagickwand-dev \  
xvfb \  
&& rm -rf /var/lib/apt/lists  
  
# manually install phantomjs  
RUN curl -sL -o -
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar -xjf - -O phantomjs-2.1.1-linux-x86_64/bin/phantomjs >
/usr/bin/phantomjs && chmod +x /usr/bin/phantomjs  
  
# install rvm  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \  
\curl -sSL https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c 'source /etc/profile.d/rvm.sh'  
  
# make bundler a default gem  
RUN echo bundler >> /usr/local/rvm/gemsets/global.gems  
  
# setup some default flags from rvm (auto install, auto gemset create, quiet
curl)  
RUN echo
"rvm_install_on_use_flag=1\nrvm_gemset_create_on_use_flag=1\nrvm_quiet_curl_flag=1"
> ~/.rvmrc  
  
# preinstall some ruby versions  
ENV PREINSTALLED_RUBIES "2.4.0 2.3.2 2.3.1 2.3.0 2.2.2 2.2.1 2.1.5 2.1.4 2.1.2
2.1.1"  
RUN /bin/bash -l -c 'for version in $PREINSTALLED_RUBIES; do echo "Now
installing Ruby $version"; rvm install $version; rvm cleanup all; done'  
  
# source rvm in every shell  
RUN sed -i '3i . /etc/profile.d/rvm.sh\n' ~/.profile  
  
# disable strict host key checking (used for deploy)  
RUN mkdir ~/.ssh  
RUN echo "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config  
  
# login shell by default so rvm is sourced automatically and 'rvm use' can be
used  
ENTRYPOINT /bin/bash -l

