FROM alpine:3.6  
  
ENV OTP_VERSION="19.3.6.1"  
  
ENV TAR_FILE="OTP-${OTP_VERSION}.tar.gz"  
ENV OTP_DOWNLOAD_URL="https://github.com/erlang/otp/archive/${TAR_FILE}"  
ENV RUN_DEPS="bash ncurses openssl"  
ENV BUILD_DEPS="autoconf gcc make musl-dev ncurses-dev openssl-dev zlib-dev"  
  
RUN set -ex \  
&& apk update \  
&& apk upgrade \  
&& apk add $RUN_DEPS \  
&& apk add $BUILD_DEPS --virtual .build-deps \  
&& wget $OTP_DOWNLOAD_URL \  
&& tar xf $TAR_FILE \  
&& rm $TAR_FILE \  
&& cd otp-OTP-$OTP_VERSION \  
&& ./otp_build autoconf \  
&& ./otp_build configure \  
\--prefix=/usr \  
\--enable-shared-zlib \  
\--enable-threads \  
\--enable-smp-support \  
\--enable-kernel-poll \  
\--enable-hipe \  
\--with-ssl \  
\--without-javac \  
\--without-megaco \  
\--without-odbc \  
\--without-wx \  
\--without-debugger \  
\--without-observer \  
\--without-orber \  
\--without-et \  
\--without-snmp \  
\--without-otp_mibs \  
\--without-os_mon \  
\--without-ssh \  
\--without-cosNotification \  
\--without-eldap \  
\--without-cosEventDomain \  
&& make -j $(grep -c ^processor /proc/cpuinfo) \  
&& make install \  
&& ln -s /usr/lib/erlang/lib/erl_interface-$(awk '$1 == "EI_VSN" {print $3}'
./lib/erl_interface/vsn.mk)/bin/erl_call /usr/bin/erl_call \  
&& cd .. \  
&& rm -r otp-OTP-$OTP_VERSION \  
&& apk del .build-deps \  
&& rm -f /var/cache/apk/*  
  
CMD ["erl"]  

