ARG APACHE_STORM_VER="latest"  
FROM fmantuano/apache-storm:${APACHE_STORM_VER}  
  
MAINTAINER Fedele Mantuano "mantuano.fedele@gmail.com"  
# environment variables  
ARG TIKA_VER="1.16"  
  
ENV FAUP_PATH="/opt/faup-master" \  
LEIN_PATH="/usr/local/bin/lein" \  
LEIN_ROOT="yes" \  
TIKA_APP_JAR="/opt/tika-app-${TIKA_VER}.jar" \  
V8_HOME="/opt/pyv8/build/v8_r19632"  
# system packages to install  
RUN set -ex; \  
apt-get -yqq update; \  
apt-get -yqq --no-install-recommends install \  
autoconf \  
automake \  
build-essential \  
cmake \  
git \  
graphviz \  
graphviz-dev \  
libboost-all-dev \  
libboost-python-dev \  
libemail-outlook-message-perl \  
libffi-dev \  
libfuzzy-dev \  
libjpeg-dev \  
libtool \  
libxml2-dev \  
libxslt-dev \  
libxslt1-dev \  
libyaml-dev \  
p7zip-full \  
pkg-config \  
python-dev \  
python-pip \  
python-setuptools \  
spamassassin \  
unrar-free \  
unzip \  
yara \  
zlib1g-dev; \  
# cleaning  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*; \  
# upgrade python tools  
pip install --upgrade pip setuptools; \  
# lein install for streamparse  
curl -So ${LEIN_PATH}
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein &&
chmod 755 ${LEIN_PATH} && lein version; \  
# Apache Tika install for SpamScope  
curl -So ${TIKA_APP_JAR} https://archive.apache.org/dist/tika/tika-
app-${TIKA_VER}.jar; \  
# Faup install for SpamScope  
git clone https://github.com/stricaud/faup.git ${FAUP_PATH} && mkdir -p
$FAUP_PATH/build && cd $FAUP_PATH/build && cmake .. && make && make install &&
echo '/usr/local/lib' | tee -a /etc/ld.so.conf.d/faup.conf && ldconfig; \  
# Thug install for Spamscope  
git clone https://github.com/buffer/pyv8.git /opt/pyv8 && cd /opt/pyv8 &&
python setup.py build && python setup.py install; \  
pip install pygraphviz --install-option="--include-path=/usr/include/graphviz"
\--install-option="--library-path=/usr/lib/graphviz/"; \  
pip install thug; \  
echo "/opt/libemu/lib/" > /etc/ld.so.conf.d/libemu.conf && ldconfig; \  
# purge packages not used  
apt-get -yqq purge \  
build-essential \  
cmake; \  
apt-get -yqq autoremove && dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg
--purge  

