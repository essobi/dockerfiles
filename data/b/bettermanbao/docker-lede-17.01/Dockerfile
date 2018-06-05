FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y software-properties-common xz-utils build-essential
ccache git libncurses5-dev libncursesw5-dev gawk wget  
  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN apt-get update  
RUN apt-get install -y libstdc++6-4.7-dev libstdc++6  
  
RUN wget https://downloads.lede-
project.org/releases/17.01.1/targets/ramips/mt7620/lede-sdk-17.01.1-ramips-
mt7620_gcc-5.4.0_musl-1.1.16.Linux-x86_64.tar.xz  
RUN tar xf lede-sdk-17.01.1-ramips-
mt7620_gcc-5.4.0_musl-1.1.16.Linux-x86_64.tar.xz  
RUN rm lede-sdk-17.01.1-ramips-
mt7620_gcc-5.4.0_musl-1.1.16.Linux-x86_64.tar.xz  
  
RUN cd lede-sdk-* \  
&& ./scripts/feeds update base \  
&& ./scripts/feeds update packages \  
&& ./scripts/feeds install libpcre libopenssl libopenssl libmbedtls \  
&& wget -P package/feeds/base/mbedtls/patches
https://github.com/bettermanbao/lede/raw/lede-17.01/package/libs/mbedtls/patches/999-tweak-
config-for-shadowsocks.patch  
  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

