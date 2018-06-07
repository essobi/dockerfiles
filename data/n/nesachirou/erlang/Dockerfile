FROM alpine:3.7  
  
RUN apk add -U \  
autoconf \  
build-base \  
curl \  
ncurses-dev \  
openjdk8 \  
openssl-dev \  
unixodbc-dev \  
unzip \  
zlib-dev  
  
ENV PATH=/usr/lib/jvm/java-1.8-openjdk/bin:$PATH  
  
RUN cd /root \  
&& curl -L https://github.com/erlang/otp/archive/OTP-19.3.6.5.zip > otp.zip \  
&& unzip otp.zip \  
&& (cd otp-* \  
&& ./otp_build autoconf \  
&& ./configure --with-ssl=/usr/include \  
&& make -j$(awk -F: '/cpu cores/{sum+=$2}END{print sum}' /proc/cpuinfo) \  
&& make -j$(awk -F: '/cpu cores/{sum+=$2}END{print sum}' /proc/cpuinfo)
install) \  
&& rm -rf otp* \  
&& apk del \  
autoconf \  
build-base \  
curl \  
unzip \  
&& rm -rf /var/cache/apk/*  

