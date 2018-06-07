FROM gliderlabs/alpine:3.4  
  
MAINTAINER Omnys srl <sistemi@omnys.com>  
  
ENV EARLANG_VERSION 18.3.2-r0  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk --no-cache add \  
erlang=${EARLANG_VERSION} \  
erlang-public-key=${EARLANG_VERSION} \  
erlang-syntax-tools=${EARLANG_VERSION} \  
erlang-erl-docgen=${EARLANG_VERSION} \  
erlang-gs=${EARLANG_VERSION} \  
erlang-observer=${EARLANG_VERSION} \  
erlang-ssh=${EARLANG_VERSION} \  
erlang-ose=${EARLANG_VERSION} \  
erlang-cosfiletransfer=${EARLANG_VERSION} \  
erlang-runtime-tools=${EARLANG_VERSION} \  
erlang-os-mon=${EARLANG_VERSION} \  
erlang-tools=${EARLANG_VERSION} \  
erlang-cosproperty=${EARLANG_VERSION} \  
erlang-common-test=${EARLANG_VERSION} \  
erlang-dialyzer=${EARLANG_VERSION} \  
erlang-edoc=${EARLANG_VERSION} \  
erlang-otp-mibs=${EARLANG_VERSION} \  
erlang-crypto=${EARLANG_VERSION} \  
erlang-costransaction=${EARLANG_VERSION} \  
erlang-odbc=${EARLANG_VERSION} \  
erlang-inets=${EARLANG_VERSION} \  
erlang-asn1=${EARLANG_VERSION} \  
erlang-snmp=${EARLANG_VERSION} \  
erlang-erts=${EARLANG_VERSION} \  
erlang-et=${EARLANG_VERSION} \  
erlang-cosnotification=${EARLANG_VERSION} \  
erlang-xmerl=${EARLANG_VERSION} \  
erlang-typer=${EARLANG_VERSION} \  
erlang-coseventdomain=${EARLANG_VERSION} \  
erlang-stdlib=${EARLANG_VERSION} \  
erlang-diameter=${EARLANG_VERSION} \  
erlang-hipe=${EARLANG_VERSION} \  
erlang-ic=${EARLANG_VERSION} \  
erlang-eunit=${EARLANG_VERSION} \  
erlang-webtool=${EARLANG_VERSION} \  
erlang-mnesia=${EARLANG_VERSION} \  
erlang-erl-interface=${EARLANG_VERSION} \  
erlang-test-server=${EARLANG_VERSION} \  
erlang-sasl=${EARLANG_VERSION} \  
erlang-jinterface=${EARLANG_VERSION} \  
erlang-kernel=${EARLANG_VERSION} \  
erlang-orber=${EARLANG_VERSION} \  
erlang-costime=${EARLANG_VERSION} \  
erlang-percept=${EARLANG_VERSION} \  
erlang-dev=${EARLANG_VERSION} \  
erlang-eldap=${EARLANG_VERSION} \  
erlang-reltool=${EARLANG_VERSION} \  
erlang-debugger=${EARLANG_VERSION} \  
erlang-ssl=${EARLANG_VERSION} \  
erlang-megaco=${EARLANG_VERSION} \  
erlang-parsetools=${EARLANG_VERSION} \  
erlang-cosevent=${EARLANG_VERSION} \  
erlang-compiler=${EARLANG_VERSION} \  
&& rm -rf /var/cache/apk/*  

