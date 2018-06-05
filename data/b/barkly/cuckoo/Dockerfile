FROM gliderlabs/alpine:3.4  
# YARA  
ENV GOSU_VERSION 1.9  
ENV SSDEEP ssdeep-2.13  
RUN apk-install openssl file jansson python tini  
RUN apk-install -t build-deps git autoconf automake file-dev flex git jansson-
dev libc-dev libtool build-base openssl-dev python-dev py-setuptools \  
&& set -x \  
&& echo "Grab gosu for easy step-down from root..." \  
&& apk-install -t .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del .gosu-deps \  
&& echo "Install Yara from source..." \  
&& cd /tmp/ \  
&& git clone \--recursive https://github.com/VirusTotal/yara.git \  
&& cd /tmp/yara \  
&& ./bootstrap.sh \  
&& ./configure --enable-cuckoo \  
\--enable-magic \  
\--with-crypto \  
&& make \  
&& make install \  
&& echo "Install yara-python..." \  
&& cd /tmp/ \  
&& git clone \--recursive https://github.com/VirusTotal/yara-python \  
&& cd yara-python \  
&& python setup.py build --dynamic-linking \  
&& python setup.py install \  
&& rm -rf /tmp/* \  
&& apk del --purge build-deps  
  
# Install Volatility Dependancies  
RUN apk-install ca-certificates zlib py-pillow py-crypto py-lxml py-setuptools  
RUN apk-install -t .build-deps \  
openssl-dev \  
python-dev \  
build-base \  
zlib-dev \  
libc-dev \  
jpeg-dev \  
automake \  
autoconf \  
py-pip \  
git \  
&& export PIP_NO_CACHE_DIR=off \  
&& export PIP_DISABLE_PIP_VERSION_CHECK=on \  
&& pip install --upgrade pip wheel \  
&& pip install simplejson \  
construct \  
openpyxl \  
haystack \  
distorm3 \  
colorama \  
ipython \  
pycoin \  
pytz \  
&& set -x \  
&& cd /tmp \  
&& echo "Installing Volatility from source..." \  
&& git clone \--recursive
https://github.com/volatilityfoundation/volatility.git \  
&& cd volatility \  
&& python setup.py build install \  
&& rm -rf /tmp/* \  
&& apk del --purge .build-deps  
  
# Install Cuckoo Sandbox Required Dependencies  
RUN apk-install tcpdump py-lxml py-chardet py-libvirt py-crypto py-psycopg2
bash  
RUN apk-install -t .build-deps \  
openssl-dev \  
libxslt-dev \  
libxml2-dev \  
python-dev \  
libffi-dev \  
build-base \  
zlib-dev \  
libc-dev \  
jpeg-dev \  
file-dev \  
automake \  
autoconf \  
libtool \  
py-pip \  
git \  
&& pip install awscli boto3 \  
&& pip install pymongo --upgrade \  
&& mkdir /root/.aws \  
&& aws configure set s3.signature_version s3v4 \  
&& set -x \  
&& echo "Install snappy" \  
&& apk --update add snappy \  
&& git clone https://github.com/google/snappy.git /snappy \  
&& cd /snappy \  
&& ./autogen.sh \  
&& ./configure && make install \  
&& export CPPFLAGS="-I/usr/local/include" && export
CFLAGS="-I/usr/local/include" \  
&& export LDFLAGS="-L/usr/local/lib" \  
&& pip install python-snappy \  
&& echo "Install ssdeep..." \  
&& wget -O /tmp/$SSDEEP.tar.gz
https://downloads.sourceforge.net/project/ssdeep/$SSDEEP/$SSDEEP.tar.gz \  
&& cd /tmp \  
&& tar zxvf $SSDEEP.tar.gz \  
&& cd $SSDEEP \  
&& ./configure \  
&& make \  
&& make install \  
&& echo "Install pydeep..." \  
&& cd /tmp \  
&& git clone https://github.com/kbandla/pydeep.git \  
&& cd pydeep \  
&& python setup.py build \  
&& python setup.py install \  
&& echo "Cloning Cuckoo Sandbox..." \  
&& git clone \--recursive --branch develop
https://github.com/barklyprotects/cuckoo.git /cuckoo \  
&& adduser -DH cuckoo \  
&& cd /cuckoo \  
&& export PIP_NO_CACHE_DIR=off \  
&& export PIP_DISABLE_PIP_VERSION_CHECK=on \  
&& pip install --upgrade pip wheel pyvmomi httpreplay \  
&& echo "Install mitmproxy..." \  
&& LDFLAGS=-L/lib pip install mitmproxy \  
&& echo "Install m2crypto..." \  
&& pip install m2crypto \  
&& LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip install -r requirements.txt" \  
&& python utils/community.py -waf \  
&& echo "Clean up unnecessary files..." \  
&& rm -rf /tmp/* \  
&& apk del --purge .build-deps  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN mkdir -p /uploads/cuckoo-tmp && \  
chown -R cuckoo:cuckoo /uploads && \  
chown -R cuckoo:cuckoo /cuckoo  
  
#data volumes  
VOLUME ["/malware"]  
VOLUME ["/rules"]  
VOLUME ["/data"]  
VOLUME ["/plugins"]  
VOLUME ["/uploads/cuckoo-tmp"]  
  
EXPOSE 1337 31337  
WORKDIR /cuckoo  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["help"]  

