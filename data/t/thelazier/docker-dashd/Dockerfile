# Dockerfile for Dashd Server  
# https://www.dash.org/  
FROM alpine as builder  
WORKDIR /  
  
RUN apk --no-cache --update add libstdc++ curl build-base git tar perl
autoconf automake libtool linux-headers patch file bash \  
&& git clone -b master --depth 1 https://github.com/dashpay/dash.git \  
&& cd dash \  
# Patch for OpenSSL 1.0.1t (from 1.0.1k)  
&& curl -s https://raw.githubusercontent.com/thelazier/docker-
dashd/master/patches/openssl1.0.1t.patch | patch -p1 \  
&& cd depends \  
&& make NO_QT=1 NO_WALLET=1 HOST=x86_64-pc-linux-gnu \  
&& cd .. \  
&& git reset --hard \  
&& ./autogen.sh \  
&& ./configure --prefix=`pwd`/depends/x86_64-pc-linux-gnu --disable-wallet \  
&& make install  
  
# Create run script  
RUN echo $'#!/usr/bin/env bash\n\  
set -x\n\  
trap '"'"'/usr/local/bin/dash-cli stop'"'"$' SIGTERM\n\  
/usr/local/bin/dashd &\n\  
while true; do sleep; done\n\  
' > /dash/depends/x86_64-pc-linux-gnu/bin/run_dashd.sh  
RUN chmod +x /dash/depends/x86_64-pc-linux-gnu/bin/run_dashd.sh  
  
# End.  
FROM alpine  
MAINTAINER TheLazieR <thelazier@gmail.com>  
LABEL description="Dockerized Dash Daemon"  
COPY \--from=builder /dash/depends/x86_64-pc-linux-gnu/. /usr/local/.  
RUN apk --no-cache --update add libstdc++ bash  
VOLUME ["/root/.dashcore"]  
ENTRYPOINT ["/usr/local/bin/run_dashd.sh"]  
EXPOSE 9998 9999 19998 19999  

