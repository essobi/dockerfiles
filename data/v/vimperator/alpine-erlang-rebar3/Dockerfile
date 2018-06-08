FROM msaraiva/erlang:17.5  
MAINTAINER Ofer Affias  
  
RUN apk --update add \  
erlang17 \  
erlang17-webtool \  
erlang17-xmerl \  
erlang17-tools \  
erlang17-typer \  
erlang17-snmp \  
erlang17-test-server \  
erlang17-syntax-tools \  
erlang17-ssl \  
erlang17-sasl \  
erlang17-runtime-tools \  
erlang17-ssh \  
erlang17-stdlib \  
erlang17-ose \  
erlang17-otp-mibs \  
erlang17-reltool \  
erlang17-mnesia \  
erlang17-percept \  
erlang17-parsetools \  
erlang17-orber \  
erlang17-public-key \  
erlang17-odbc \  
erlang17-os-mon \  
erlang17-observer \  
erlang17-et \  
erlang17-ic \  
erlang17-megaco \  
erlang17-kernel \  
erlang17-hipe \  
erlang17-inets \  
erlang17-jinterface \  
erlang17-erts \  
erlang17-gs \  
erlang17-eunit \  
erlang17-debugger \  
erlang17-costime \  
erlang17-costransaction \  
erlang17-erl-interface \  
erlang17-edoc \  
erlang17-dialyzer \  
erlang17-eldap \  
erlang17-diameter \  
erlang17-erl-docgen \  
erlang17-crypto \  
erlang17-cosevent \  
erlang17-cosnotification \  
erlang17-asn1 \  
erlang17-cosfiletransfer \  
erlang17-coseventdomain \  
erlang17-dev \  
erlang17-common-test \  
erlang17-compiler \  
erlang17-cosproperty \  
&& rm -rf /var/cache/apk/*  
  
ENV REBAR_VERSION beta-1  
  
ADD https://github.com/rebar/rebar3/archive/${REBAR_VERSION}.tar.gz \  
/usr/src/rebar3-${REBAR_VERSION}.tar.gz  
RUN cd /usr/src \  
&& tar zxf rebar3-${REBAR_VERSION}.tar.gz \  
&& cd rebar3-${REBAR_VERSION} \  
&& escript bootstrap \  
&& cp rebar3 /usr/bin/rebar3 \  
&& rm -rf /usr/src/rebar3-${REBAR_VERSION}*  
  
CMD ["/bin/sh"]

