FROM ubuntu:14.04  
RUN rm /etc/apt/sources.list \  
&& touch "/etc/apt/sources.list" \  
&& echo "deb http://mirrors.ustc.edu.cn/ubuntu/ trusty main restricted
universe multiverse" >> "/etc/apt/sources.list" \  
&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty main restricted
universe multiverse" >> "/etc/apt/sources.list" \  
&& echo "deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-security main
restricted universe multiverse" >> "/etc/apt/sources.list" \  
&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-security main
restricted universe multiverse" >> "/etc/apt/sources.list" \  
&& echo "deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-updates main restricted
universe multiverse" >> "/etc/apt/sources.list" \  
&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-updates main
restricted universe multiverse" >> "/etc/apt/sources.list" \  
&& echo "deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-backports main
restricted universe multiverse" >> "/etc/apt/sources.list" \  
&& echo "deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-backports main
restricted universe multiverse" >> "/etc/apt/sources.list" \  
&& sudo apt-get update \  
&& sudo apt-get install -y nano python git wget make libtool automake pkg-
config python-pip software-properties-common python-software-properties \  
# installing libsodium, needed for toxcore  
&& git clone https://github.com/jedisct1/libsodium.git \  
&& cd libsodium && git checkout tags/1.0.3 && ./autogen.sh && ./configure
--prefix=/usr && make && make install && cd ../ && rm -rf libsodium \  
# installing libopus, needed for audio encoding/decoding  
&& apt-get install -y libopus* \  
# installing vpx  
&& apt-get install -y yasm libvpx* \  
# creating librarys' links and updating cache  
&& ldconfig \  
&& git clone https://github.com/TokTok/c-toxcore \  
&& cd c-toxcore && autoreconf -i && mkdir _build && cd _build && ../configure
\  
&& make -j4 && make install && cd .. && rm -rf c-toxcore \  
#Install Golang toxtun  
&& wget https://redirector.gvt1.com/edgedl/go/go1.9.2.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf go*.gz \  
&& rm -rf go*.gz \  
&& echo "\nexport PATH=$PATH:/usr/local/go/bin" >> /etc/profile \  
&& export PATH=$PATH:/usr/local/go/bin \  
#reboot and not reboot  
&& export GOPATH=/root/go \  
&& mkdir /root/go \  
&& go get -u github.com/kitech/go-toxcore \  
&& go get -u github.com/kitech/goplusplus \  
&& go get -u github.com/cyfdecyf/color \  
&& go get -u github.com/bitly/go-simplejson \  
&& go get -u github.com/GianlucaGuarini/go-observable \  
&& go get -u github.com/go-ini/ini \  
&& go get -u golang.org/x/net/icmp \  
&& go get -u github.com/tatsushid/go-fastping \  
&& go get -u github.com/kitech/toxtun \  
&& ldconfig  

