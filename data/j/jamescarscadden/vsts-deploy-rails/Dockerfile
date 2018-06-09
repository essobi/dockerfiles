FROM ubuntu:16.04  
MAINTAINER James Carscadden <james@carscadden.org>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r railsapp && useradd -r -g railsapp railsapp  
  
# supress debconf  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Prepare for software installs  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates\  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add more up to date Node sources  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
# Add more up to date Postgres sources  
RUN echo "deb https://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/postgres.list  
RUN curl -sL https://postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -  
  
# install the prerequisite patches here so that rvm will install under non-
root account.  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
bison \  
expect \  
g++ \  
gawk \  
gcc \  
git \  
libc6-dev \  
libffi-dev \  
libgdbm-dev \  
libgmp-dev \  
libncurses5-dev \  
libreadline6-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libyaml-dev \  
make \  
nodejs \  
patch \  
pkg-config \  
postgresql-server-dev-9.6 \  
postgresql-client-9.6 \  
sqlite3 \  
unzip \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# INSTALL bower  
RUN npm install bower -g  
  
# Allow bower to run as root without the warning  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  

