FROM ubuntu:14.04  
  
ENV OTP_VERSION=18.0 LANG=C.UTF-8  
  
RUN apt-get update \  
&& apt-get install -y wget unixodbc-dev build-essential autoconf m4
libncurses5-dev \  
&& wget "https://github.com/erlang/otp/archive/OTP-$OTP_VERSION.tar.gz"
\--quiet --output-document=otp-src.tar.gz \  
&& mkdir -p /usr/src/otp-src \  
&& tar -xzf otp-src.tar.gz -C /usr/src/otp-src --strip-components=1 \  
&& rm otp-src.tar.gz \  
&& cd /usr/src/otp-src \  
&& ./otp_build autoconf \  
&& ./configure \  
&& make -j$(nproc) \  
&& make install \  
&& rm -rf /usr/src/otp-src /var/lib/apt/lists/*  
  
  
CMD ["erl"]  

