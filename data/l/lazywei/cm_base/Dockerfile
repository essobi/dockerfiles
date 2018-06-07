FROM ubuntu:14.10  
MAINTAINER Bert Chang "https://github.com/lazywei"  
# We use bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
RUN apt-get install -y git curl wget zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties autoconf ruby bison  
  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN /root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
  
ENV CONFIGURE_OPTS --disable-install-doc  
  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
  
# Prepare source folders  
RUN mkdir -p /root/src  
  
# Install postgresql tools  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
  
# Add PostgreSQL's repository. It contains the most recent stable release  
# of PostgreSQL, ``9.3``.  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
# Install ``python-software-properties``, ``software-properties-common`` and
PostgreSQL 9.3  
# There are some warnings (in red) that show up during the build. You can hide  
# them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3
postgresql-server-dev-9.3 libpq-dev  

