FROM blacktop/volatility:2.6  
LABEL maintainer "Carlos Ortigoza Dempster <carlos.otgz@gmail.com>"  
  
ENV CUCKOO_VERSION 2.0.4a1  
ENV CUCKOO_CWD /cuckoo  
ENV SSDEEP ssdeep-2.13  
# Install Cuckoo Sandbox Required Dependencies  
COPY requirements.txt /tmp/requirements.txt  
RUN apk add --no-cache tcpdump py-lxml py-chardet py-libvirt py-crypto curl
swig libpq openvpn  
RUN apk add --no-cache -t .build-deps \  
postgresql-dev \  
libxslt-dev \  
libxml2-dev \  
python-dev \  
libffi-dev \  
build-base \  
libstdc++ \  
zlib-dev \  
libc-dev \  
jpeg-dev \  
file-dev \  
automake \  
autoconf \  
libtool \  
py-pip \  
git \  
linux-headers \  
libcap \  
&& set -x \  
&& setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump \  
&& echo "===> Install ssdeep..." \  
&& wget -O /tmp/$SSDEEP.tar.gz
https://downloads.sourceforge.net/project/ssdeep/$SSDEEP/$SSDEEP.tar.gz \  
&& cd /tmp \  
&& tar zxvf $SSDEEP.tar.gz \  
&& cd $SSDEEP \  
&& ./configure \  
&& make \  
&& make install \  
&& echo "===> Install pydeep..." \  
&& cd /tmp \  
&& git clone https://github.com/kbandla/pydeep.git \  
&& cd pydeep \  
&& python setup.py build \  
&& python setup.py install \  
&& echo "===> Install Cuckoo Sandbox..." \  
&& mkdir /cuckoo \  
&& adduser -D -h /cuckoo cuckoo \  
&& export PIP_NO_CACHE_DIR=off \  
&& export PIP_DISABLE_PIP_VERSION_CHECK=on \  
&& pip install --upgrade pip wheel \  
&& LDFLAGS=-L/lib pip install cuckoo==$CUCKOO_VERSION \  
&& cuckoo \  
&& cuckoo community \  
&& echo "===> Install mitmproxy..." \  
&& LDFLAGS=-L/lib pip install mitmproxy \  
&& pip install -r /tmp/requirements.txt \  
&& echo "===> Clean up unnecessary files..." \  
&& rm -rf /tmp/* \  
&& apk del --purge .build-deps  
  
COPY check_required_services.py /check_required_services.py  
COPY docker-entrypoint.sh /entrypoint.sh  
  
WORKDIR /cuckoo  
  
VOLUME ["/cuckoo/conf"]  
  
EXPOSE 1337 2042 31337  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["--help"]  

