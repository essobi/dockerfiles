FROM debian:jessie  
MAINTAINER danielguerra, https://github.com/danielguerra  
ENV LIBTOOL libtool-2.4.2  
RUN addgroup wireshark  
RUN useradd -m -g wireshark wireshark  
RUN apt-get update -qq  
RUN apt-get install -yq build-essential autoconf automake bison flex \  
libpcap-dev libglib2.0-dev libgeoip-dev libkrb5-dev git-core sudo \  
qt5-default libssl-dev libgtk-3-dev ca-certificates wget libtool \  
qttools5-dev-tools liblua5.2-dev libgnutls28-dev libssh-dev libsbc-dev\  
portaudio19-dev libgcrypt-dev libcap-dev libsmi-dev libc-ares-dev \  
\--no-install-recommends \  
&& cd /tmp \  
&& wget --no-check-certificate https://ftp.gnu.org/gnu/libtool/$LIBTOOL.tar.gz
\  
&& tar zxf $LIBTOOL.tar.gz && cd $LIBTOOL && ./configure && make && make
install && ldconfig \  
&& cd /tmp \  
&& git clone \--recursive https://github.com/wireshark/wireshark.git \  
&& cd /tmp/wireshark \  
&& ./autogen.sh \  
&& ./configure --with-ssl --enable-tfshark --with-dumpcap-group=wireshark
--enable-setcap-install \  
&& make && make install && ldconfig \  
&& echo "wireshark:wireshark" > /tmp/pass && /usr/sbin/chpasswd < /tmp/pass \  
&& echo "wireshark ALL=(ALL) ALL" >> /etc/sudoers \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN setcap cap_net_raw,cap_net_admin=eip /usr/local/bin/dumpcap  
RUN usermod -a -G wireshark wireshark  
RUN chgrp wireshark /usr/local/bin/dumpcap  
RUN chmod 750 /usr/local/bin/dumpcap  
USER wireshark  
CMD ["/bin/bash"]  

