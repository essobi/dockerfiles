FROM alpine:3.7  
ARG DISABLED_APPS='megaco wx debugger jinterface orber reltool observer gs et'  
ARG ERLANG_TAG=master  
ARG ELIXIR_TAG=master  
  
LABEL erlang_version=$ERLANG_TAG erlang_disabled_apps=$DISABLED_APPS
elixir_version=$ELIXIR_TAG maintainer="leif@leif.io"  
  
RUN apk --update add --virtual run-dependencies ca-certificates ncurses
openssl unixodbc  
  
# Install Erlang  
RUN set -xe \  
&& apk --update add --virtual erlang-build-dependencies git ca-certificates
build-base autoconf perl ncurses-dev openssl-dev unixodbc-dev tar \  
&& cd /tmp \  
&& git clone \--branch $ERLANG_TAG \--depth=1 --single-branch
https://github.com/erlang/otp.git \  
&& cd otp \  
&& echo "ERLANG_BUILD=$(git rev-parse HEAD)" >> /info.txt \  
&& echo "ERLANG_VERSION=$(cat OTP_VERSION)" >> /info.txt \  
&& for lib in ${DISABLED_APPS} ; do touch lib/${lib}/SKIP ; done \  
&& ./otp_build autoconf \  
&& ./configure \  
\--enable-smp-support \  
\--enable-m64-build \  
\--disable-native-libs \  
\--enable-sctp \  
\--enable-threads \  
\--enable-kernel-poll \  
\--disable-hipe \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& find /usr/local -regex
'/usr/local/lib/erlang/\\(lib/\|erts-\\).*/\\(man\|doc\|src\|obj\|c_src\|emacs\|info\|examples\\)'
| xargs rm -rf \  
&& rm -rf \  
/usr/local/lib/erlang/erts*/lib/lib*.a \  
/usr/local/lib/erlang/usr/lib/lib*.a \  
/usr/local/lib/erlang/lib/*/lib/lib*.a \  
&& scanelf --nobanner -E ET_EXEC -BF '%F' \--recursive /usr/local | xargs -r
strip --strip-all \  
&& scanelf --nobanner -E ET_DYN -BF '%F' \--recursive /usr/local | xargs -r
strip --strip-unneeded \  
&& apk del erlang-build-dependencies \  
&& ls -d /usr/local/lib/erlang/lib/*/src | xargs rm -rf \  
&& rm -rf \  
/opt \  
/var/cache/apk/* \  
/tmp/*  
  
# Install Elixir  
RUN apk --update add --virtual elixir-build-dependencies git build-base \  
&& cd /tmp \  
&& git clone \--branch $ELIXIR_TAG \--depth=1 --single-branch
https://github.com/elixir-lang/elixir.git \  
&& cd elixir \  
&& echo "ELIXIR_BUILD=$(git rev-parse HEAD)" >> /info.txt \  
&& echo "ELIXIR_VERSION=$(cat VERSION)" >> /info.txt \  
&& make -j$(getconf _NPROCESSORS_ONLN) compile \  
&& rm -rf .git \  
&& make install \  
&& apk del elixir-build-dependencies \  
&& rm -rf \  
/var/cache/apk/* \  
/tmp/*  
  
RUN echo cat /info.txt  
RUN echo $ELIXIR_VERSION  
  
RUN mix local.hex --force  
RUN mix local.rebar --force  
RUN mix hex.info  
  
CMD ["/bin/sh"]  

