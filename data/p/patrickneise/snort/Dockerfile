FROM alpine:3.6  
  
# Default interface, can be overidden at runtime  
ENV INTERFACE='eth0'  
# pid file location for pulledpork HUP of snort on rule update  
ENV PID_FILE=/var/run/snort_$INTERFACE  
# Default HOME_NET, can be overridden at runtime  
ENV HOME_NET=192.168.1.0/24  
# Placehoder for oinkcode if not provided at runtime  
ENV OINKCODE=<oinkcode>  
  
# Install runtime dependencies  
RUN apk add \--no-cache tini \  
perl-net-ssleay \  
perl-crypt-ssleay \  
perl-libwww \  
perl-lwp-useragent-determined \  
perl-lwp-protocol-https \  
pcre \  
libpcap \  
libdnet \  
daq \  
zlib \  
perl  
  
# Install all dependencies as build dependencies and cleanup at the end  
RUN apk add \--no-cache --virtual .build-deps \  
libpcap-dev \  
libdnet-dev \  
pcre-dev \  
daq-dev \  
bison \  
flex \  
zlib-dev \  
ca-certificates \  
openssl \  
libressl-dev \  
nghttp2-libs \  
libtirpc-dev \  
curl \  
cmake \  
make \  
wget \  
g++  
  
  
  
# Install and configure Snort and Pulled Pork then clean up  
# Using on large RUN command to minimize layers  
RUN ln -s /usr/include/tirpc/rpc /usr/include/rpc && \  
ln -s /usr/include/tirpc/netconfig.h /usr/include/netconfig.h && \  
mkdir ~/snort_src && \  
cd ~/snort_src && \  
wget https://snort.org/downloads/snort/snort-2.9.9.0.tar.gz && \  
tar -xvzf snort-2.9.9.0.tar.gz && \  
cd snort-2.9.9.0 && \  
./configure --enable-sourcefire && \  
make && \  
make install && \  
ln -s /usr/local/bin/snort /usr/sbin/snort && \  
addgroup -S snort && \  
adduser -S snort -g snort && \  
mkdir /etc/snort && \  
mkdir /etc/snort/rules && \  
mkdir /etc/snort/rules/iplists && \  
mkdir /etc/snort/preproc_rules && \  
mkdir /usr/local/lib/snort_dynamicrules && \  
mkdir /etc/snort/so_rules && \  
touch /etc/snort/rules/iplists/black_list.rules && \  
touch /etc/snort/rules/iplists/white_list.rules && \  
touch /etc/snort/rules/local.rules && \  
touch /etc/snort/sid-msg.map && \  
mkdir /var/log/snort && \  
mkdir /var/log/snort/archived_logs && \  
chmod -R 5775 /etc/snort && \  
chmod -R 5775 /var/log/snort && \  
chmod -R 5775 /var/log/snort/archived_logs && \  
chmod -R 5775 /etc/snort/so_rules && \  
chmod -R 5775 /usr/local/lib/snort_dynamicrules && \  
chown -R snort:snort /etc/snort && \  
chown -R snort:snort /var/log/snort && \  
chown -R snort:snort /usr/local/lib/snort_dynamicrules && \  
cd ~/snort_src/snort-2.9.9.0/etc/ && \  
cp *.conf* /etc/snort && \  
cp *.map /etc/snort && \  
cp *.dtd /etc/snort && \  
cd ~/snort_src/snort-2.9.9.0/src/dynamic-
preprocessors/build/usr/local/lib/snort_dynamicpreprocessor/ && \  
cp * /usr/local/lib/snort_dynamicpreprocessor/ && \  
sed -i \  
-e 's#^var RULE_PATH.*#var RULE_PATH /etc/snort/rules#' \  
-e 's#^var SO_RULE_PATH.*#var SO_RULE_PATH $RULE_PATH/so_rules#' \  
-e 's#^var PREPROC_RULE_PATH.*#var PREPROC_RULE_PATH $RULE_PATH/preproc_rules#' \  
-e 's#^var WHITE_LIST_PATH.*#var WHITE_LIST_PATH $RULE_PATH/iplists#' \  
-e 's#^var BLACK_LIST_PATH.*#var BLACK_LIST_PATH $RULE_PATH/iplists#' \  
-e 's/^\\(include $.*\\)/# \1/' \  
-e '$a\\\ninclude $RULE_PATH/local.rules' \  
-e 's!^# \\(config logdir:\\)!\1 /var/log/snort!' \  
/etc/snort/snort.conf && \  
cd ~/snort_src && \  
wget https://github.com/shirkdog/pulledpork/archive/master.tar.gz -O
pulledpork-master.tar.gz && \  
tar xvzf pulledpork-master.tar.gz && \  
cd pulledpork-master/ && \  
cp pulledpork.pl /usr/local/bin && \  
chmod +x /usr/local/bin/pulledpork.pl && \  
cp ./etc/*.conf /etc/snort/ && \  
apk del .build-deps && \  
rm -rf ~/snort_src  
  
# Copy configure pulledpork.conf  
COPY /files/pulledpork.conf /etc/snort/pulledpork.conf  
  
# Update community rules for Snort  
RUN /usr/local/bin/pulledpork.pl -c /etc/snort/pulledpork.conf  
  
# Copy local.rules  
COPY /files/local.rules /etc/snort/rules/local.rules  
  
# Entrypoint script for runtime config and starting snort  
COPY entrypoint.sh /  
  
# Shared volume for reading pcap to process  
VOLUME ["/pcap"]  
  
# Shared volume to output logs  
VOLUME ["/var/log/snort"]  
  
# Use tini as init  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]

