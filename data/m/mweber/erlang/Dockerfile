FROM ubuntu:trusty  
  
ENV OTP_VERSION="R16B02"  
  
RUN set -xe \  
&&
OTP_DOWNLOAD_URL="https://github.com/erlang/otp/archive/OTP_$OTP_VERSION.tar.gz"
\  
&&
OTP_DOWNLOAD_SHA256="d121c063fe5253b408658a0fcf5f24254d2194fc1292f9c86c7f5e4ccf48c8ad"
\  
&& buildDeps='build-essential libssl-dev libncurses5-dev m4' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& apt-get install -y --no-install-recommends curl autoconf \  
&& curl -fSLk -o otp-src.tar.gz "$OTP_DOWNLOAD_URL" \  
&& echo "$OTP_DOWNLOAD_SHA256 otp-src.tar.gz" | sha256sum -c - \  
&& mkdir -p /usr/src/otp-src \  
&& tar -xzf otp-src.tar.gz -C /usr/src/otp-src --strip-components=1 \  
&& rm otp-src.tar.gz \  
&& cd /usr/src/otp-src \  
&& ./otp_build autoconf \  
&& ./configure --disable-hipe --without-odbc \  
&& make -j$(nproc) \  
&& make install \  
&& find /usr/local -name examples |xargs rm -rf \  
&& rm -rf /usr/src/otp-src /var/lib/apt/lists/*  
  
CMD ["erl"]  
  
ENV REBAR_VERSION="2.6.1"  
  
RUN set -xe \  
&&
REBAR_DOWNLOAD_URL="https://github.com/rebar/rebar/archive/${REBAR_VERSION##*@}.tar.gz"
\  
&&
REBAR_DOWNLOAD_SHA256="aed933d4e60c4f11e0771ccdb4434cccdb9a71cf8b1363d17aaf863988b3ff60"
\  
&& mkdir -p /usr/src/rebar-src \  
&& curl -fSLk -o rebar-src.tar.gz "$REBAR_DOWNLOAD_URL" \  
&& echo "$REBAR_DOWNLOAD_SHA256 rebar-src.tar.gz" | sha256sum -c - \  
&& tar -xzf rebar-src.tar.gz -C /usr/src/rebar-src --strip-components=1 \  
&& rm rebar-src.tar.gz \  
&& cd /usr/src/rebar-src \  
&& ./bootstrap \  
&& install -v ./rebar /usr/local/bin/ \  
&& rm -rf /usr/src/rebar-src  
  
ENV REBAR3_VERSION="3.0.0"  
  
  
RUN set -xe \  
&&
REBAR3_DOWNLOAD_URL="https://github.com/erlang/rebar3/archive/${REBAR3_VERSION##*@}.tar.gz"
\  
&&
REBAR3_DOWNLOAD_SHA256="886acd7bb7cfb99d105d9f900b93f8cc6e571330838004a75b6bac2a4ac1baca"
\  
&& mkdir -p /usr/src/rebar3-src \  
&& curl -fSLk -o rebar3-src.tar.gz "$REBAR3_DOWNLOAD_URL" \  
&& echo "$REBAR3_DOWNLOAD_SHA256 rebar3-src.tar.gz" | sha256sum -c - \  
&& tar -xzf rebar3-src.tar.gz -C /usr/src/rebar3-src --strip-components=1 \  
&& rm rebar3-src.tar.gz \  
&& cd /usr/src/rebar3-src \  
&& HOME=$PWD ./bootstrap \  
&& install -v ./rebar3 /usr/local/bin/ \  
&& rm -rf /usr/src/rebar3-src  

