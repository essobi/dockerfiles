FROM alpine:3.4  
LABEL com.tomasbasham.maintainer "Tomas Basham <me@tomasbasham.co.uk>" \  
com.tomasbasham.version "18.3.2-r0" \  
com.tomasbasham.description "Erlang"  
  
ENV VERSION 18.3.2-r0  
ENV REBAR_VERSION 3.2.0  
# Install erlang and rebar  
RUN apk add --no-cache --virtual .build-deps curl \  
&& apk add --no-cache erlang erlang-asn1 erlang-common-test erlang-compiler
erlang-cosevent erlang-coseventdomain \  
erlang-cosfiletransfer erlang-cosnotification erlang-cosproperty erlang-
costime erlang-costransaction erlang-crypto \  
erlang-debugger erlang-dev erlang-dialyzer erlang-diameter erlang-edoc erlang-
eldap erlang-erl-docgen \  
erlang-erl-interface erlang-erts erlang-et erlang-eunit erlang-gs erlang-hipe
erlang-ic erlang-inets \  
erlang-jinterface erlang-kernel erlang-megaco erlang-mnesia erlang-observer
erlang-odbc erlang-orber erlang-os-mon \  
erlang-ose erlang-otp-mibs erlang-parsetools erlang-percept erlang-public-key
erlang-reltool erlang-runtime-tools \  
erlang-sasl erlang-snmp erlang-ssh erlang-ssl erlang-stdlib erlang-syntax-
tools erlang-test-server erlang-tools \  
erlang-typer erlang-webtool erlang-xmerl \  
&& curl -o rebar3-${REBAR_VERSION}.tar.gz -sSL
https://github.com/erlang/rebar3/archive/${REBAR_VERSION}.tar.gz \  
&& tar -zxf rebar3-${REBAR_VERSION}.tar.gz \  
&& cd rebar3-${REBAR_VERSION} \  
&& ./bootstrap \  
&& mv ./rebar3 /usr/bin/rebar3 \  
&& apk del .build-deps \  
&& rm -rf /rebar-${REBAR_VERSION}.tar.gz /rebar-${REBAR_VERSION} /tmp/*
/var/cache/apk/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/usr/bin/erl"]  

