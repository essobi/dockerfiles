FROM centos:6  
MAINTAINER Vinson Zou <vinsoncou@gmail.com>  
  
WORKDIR /root  
COPY rsyslog.repo /etc/yum.repos.d  
  
ENV RSYSLOG_VERSION=8.18.0 \  
PKG_CONFIG_PATH=/lib64/pkgconfig/ \  
BASE_PACKAGES="wget git automake libtool autoconf byacc pcre-devel zlib-devel
gperf" \  
BUILD_DEP_PACKAGES="libevent-devel tokyocabinet-devel pcre-devel json-c-devel
glib2-devel libfastjson-devel libestr-devel liblogging-devel flex" \  
INSTALL_PACKAGES="rsyslog"  
# build libgrok.so and mmgrok.so  
RUN yum -y install $BASE_PACKAGES $INSTALL_PACKAGES $BUILD_DEP_PACKAGES \  
&& git clone https://github.com/jordansissel/grok.git \  
&& cd grok && make && make install \  
&& cd /usr/lib64 && mv /usr/lib/libgrok.so . && ln -s libgrok.so libgrok.so.1
\  
&& cd /root \  
&& wget -q
https://github.com/rsyslog/rsyslog/archive/v${RSYSLOG_VERSION}.tar.gz -O
rsyslog.tar.gz \  
&& tar zxf rsyslog.tar.gz \  
&& mv rsyslog-${RSYSLOG_VERSION} rsyslog \  
&& cd rsyslog \  
&& ./autogen.sh --enable-mmgrok --disable-uuid --disable-liblogging-stdlog
--disable-libgcrypt \  
&& make \  
&& { \  
echo '#!/bin/sh'; \  
echo 'cp /root/rsyslog/contrib/mmgrok/.libs/mmgrok.so /data'; \  
echo 'cp /usr/lib64/libgrok.so /data'; \  
echo 'cp /usr/share/grok/patterns/base /data'; \  
} > /usr/local/bin/copy2volume \  
&& chmod a+x /usr/local/bin/copy2volume  
  
# copy file to the volume dir  
VOLUME ["/data"]  
CMD ["copy2volume"]  

