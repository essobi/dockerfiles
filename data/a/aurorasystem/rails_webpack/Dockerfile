FROM ruby:2.3  
MAINTAINER Aurora System <it@aurora-system.com>  
  
# see update.sh for why all "apt-get install"s have to stay as one long line  
ENV PYTHON_VERSION 3.6.2  
  
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D  
  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
ENV PYTHON_PIP_VERSION 9.0.1  
  
RUN set -ex \  
&& buildDeps=' \  
dpkg-dev \  
tcl-dev \  
tk-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& wget -O python.tar.xz
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz"
\  
&& wget -O python.tar.xz.asc
"https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify python.tar.xz.asc python.tar.xz \  
&& rm -rf "$GNUPGHOME" python.tar.xz.asc \  
&& mkdir -p /usr/src/python \  
&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \  
&& rm python.tar.xz \  
\  
&& cd /usr/src/python \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--enable-loadable-sqlite-extensions \  
\--enable-shared \  
\--with-system-expat \  
\--with-system-ffi \  
\--without-ensurepip \  
&& make -j "$(nproc)" \  
&& make install \  
&& ldconfig \  
\  
&& apt-get purge -y --auto-remove $buildDeps \  
\  
&& rm -rf /usr/src/python &&\  
##  
# make some useful symlinks that are expected to exist  
cd /usr/local/bin \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config &&\  
  
set -ex; \  
\  
wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \  
\  
python get-pip.py \  
\--disable-pip-version-check \  
\--no-cache-dir \  
"pip==$PYTHON_PIP_VERSION" \  
; \  
pip --version; \  
\  
rm -f get-pip.py &&\  
  
apt-get update && apt-get install -y bzip2 && \  
# see http://guides.rubyonrails.org/command_line.html#rails-dbconsole  
apt-get install -y mysql-client sqlite3 --no-install-recommends && \  
  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y
nodejs --no-install-recommends && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install yarn && \  
# Libzmq3-dev, for MySQL  
apt-get install -y libzmq3-dev && \  
# install dependencies  
apt-get install -y \  
python-tk && \  
rm -rf /var/lib/apt/lists/* &&\  
# install python-pptx  
pip install python-pptx &&\  
pip install numpy &&\  
pip install matplotlib &&\  
pip install Image &&\  
pip install coloredlogs &&\  
  
mkdir -p /app/  
  
RUN apt-get update && apt-get -y -q install ure openjdk-7-jre fonts-opensymbol
hyphen-fr hyphen-de hyphen-en-us hyphen-it hyphen-ru fonts-dejavu fonts-
dejavu-core fonts-dejavu-extra fonts-droid fonts-dustin fonts-f500 fonts-
fanwood fonts-freefont-ttf fonts-liberation fonts-lmodern fonts-lyx fonts-sil-
gentium fonts-texgyre fonts-tlwg-purisa && apt-get -q -y remove libreoffice-
gnome &&\  
wget -c 'https://aurorasystem-
my.sharepoint.com/:u:/g/personal/zhen_guo_aurora-
system_com/ESsN1S3fL2BBldRduIyyK3wBJupE2D98wf9ymoj1xsUaSQ?e=d27fdd3cd3b54c9685c446eedf1afe50'
-O libreoffice.tar.gz &&\  
tar -xvf libreoffice.tar.gz &&\  
cd LibreOffice_5.4.3.2_Linux_x86-64_deb/DEBS &&\  
dpkg -i *.deb &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* &&\  
rm -rf libreoffice.tar.gz &&\  
rm -rf LibreOffice_5.4.2.2_Linux_x86-64_deb  
  
COPY ./phantomjs /usr/bin/phantomjs  
  
# Bundle  
COPY ./Gemfile* /app/  
COPY ./package.json /app/  
  
RUN \  
cd /app && \  
gem install bundler --no-doc --no-ri && \  
bundle install && \  
yarn  
  
WORKDIR /app  
  
  

