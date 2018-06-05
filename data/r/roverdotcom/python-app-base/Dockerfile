FROM ubuntu:16.04  
  
ARG snagsby_version=0.1.5  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
curl \  
geoip-database \  
git \  
graphviz \  
ipython \  
libffi-dev \  
libfreetype6-dev \  
libgdal-dev \  
libgeoip1 \  
libgeos-dev \  
libjpeg-dev \  
liblcms2-dev \  
libmemcached-dev \  
libmysqlclient-dev \  
libpq-dev \  
libproj-dev \  
libspatialite-dev \  
libsqlite3-dev \  
libsqlite3-mod-spatialite \  
libssl-dev \  
libtiff5-dev \  
libxslt1-dev \  
mysql-client \  
python-dev \  
python-pyexiv2 \  
python-tidylib \  
ruby-dev \  
swig \  
time \  
vim \  
wget \  
zlib1g-dev \  
zlib1g-dev \  
zlibc \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -L
https://github.com/roverdotcom/snagsby/releases/download/v${snagsby_version}/snagsby-${snagsby_version}.linux-
amd64.tar.gz \  
| tar -C /usr/local/bin -zxf -  
  
# Postgres packages from the official repo  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >> \  
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc \  
| apt-key add - \  
&& apt-get update && apt-get install -y \  
postgresql-client-9.4 \  
&& rm -rf /var/lib/apt/lists/*  
  
# Upgrade pip  
RUN curl -o /get-pip.py https://bootstrap.pypa.io/get-pip.py \  
&& python /get-pip.py \  
&& rm /get-pip.py  
RUN pip install --upgrade --force setuptools  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm -g install \  
uglify-js \  
phantomjs-prebuilt \  
jasmine-node \  
postcss-cli \  
autoprefixer \  
clean-css  
  
RUN gem install --no-rdoc --no-ri sass --version 3.4.5 \  
&& gem install --no-rdoc --no-ri compass --version 1.0.1  

