FROM ubuntu:trusty  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' 9.6 >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv 68576280 \  
&& echo 'deb http://deb.nodesource.com/node_8.x trusty main' >
/etc/apt/sources.list.d/nodesource.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv 46C2130DFD2497F5 \  
&& echo 'deb http://dl.yarnpkg.com/debian/ stable main' >
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
locales \  
make \  
gcc \  
g++ \  
curl \  
less \  
libxml2-dev \  
libxslt-dev \  
pkg-config \  
libcurl3-dev \  
libpq-dev \  
libgmp3-dev \  
postgresql-client-9.6 \  
git-core \  
ssh \  
libmagickcore-dev \  
libmagickwand-dev \  
imagemagick \  
libsqlite3-dev \  
catdoc \  
enca \  
ca-certificates \  
libmysqlclient-dev \  
nodejs \  
build-essential \  
yarn \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& truncate -s 0 /var/log/*log  
  
RUN echo "Asia/Yekaterinburg" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
ENV RVM_PATH /usr/local/rvm  
ENV RVM ${RVM_PATH}/bin/rvm  
ENV RVM_RUBY ruby-2.2.7  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 \  
&& (\curl -ksSL https://get.rvm.io | bash -s stable)  
RUN $RVM install $RVM_RUBY  
ENV GEM_HOME /gems  
ENV GEM_PATH ${GEM_HOME}  
ENV PATH ${RVM_PATH}/rubies/${RVM_RUBY}/bin:${GEM_HOME}/bin:$PATH  
ENV BUNDLE_SILENCE_ROOT_WARNING 1  
# https://github.com/bundler/bundler/issues/4402  
RUN echo 'gem: --no-rdoc --no-ri --no-document' > /root/.gemrc \  
&& ssh-keyscan -H github.com >> /etc/ssh/ssh_known_hosts \  
&& gem update --system 2.6.1 \  
&& gem install bundler --version 1.16.2 \  
&& bundle config --global jobs 7 \  
&& bundle config git.allow_insecure true \  
&& bundle config --global build.nokogiri --use-system-libraries  
  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
  
ENTRYPOINT ["/tini", "--"]  
  
WORKDIR /app  

