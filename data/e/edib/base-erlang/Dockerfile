FROM edib/base-dev:3.6  
MAINTAINER Christoph Grabo <edib@markentier.com>  
  
RUN apk --no-cache upgrade && apk --no-cache add \  
'erlang<20' \  
'erlang-asn1<20' \  
'erlang-common-test<20' \  
'erlang-compiler<20' \  
'erlang-cosevent<20' \  
'erlang-coseventdomain<20' \  
'erlang-cosfiletransfer<20' \  
'erlang-cosnotification<20' \  
'erlang-cosproperty<20' \  
'erlang-costime<20' \  
'erlang-costransaction<20' \  
'erlang-crypto<20' \  
'erlang-debugger<20' \  
'erlang-dev<20' \  
'erlang-dialyzer<20' \  
'erlang-diameter<20' \  
'erlang-edoc<20' \  
'erlang-eldap<20' \  
'erlang-erl-docgen<20' \  
'erlang-erl-interface<20' \  
'erlang-erts<20' \  
'erlang-et<20' \  
'erlang-eunit<20' \  
'erlang-gs<20' \  
'erlang-hipe<20' \  
'erlang-ic<20' \  
'erlang-inets<20' \  
'erlang-jinterface<20' \  
'erlang-kernel<20' \  
'erlang-megaco<20' \  
'erlang-mnesia<20' \  
'erlang-observer<20' \  
'erlang-odbc<20' \  
'erlang-orber<20' \  
'erlang-os-mon<20' \  
'erlang-otp-mibs<20' \  
'erlang-parsetools<20' \  
'erlang-percept<20' \  
'erlang-public-key<20' \  
'erlang-reltool<20' \  
'erlang-runtime-tools<20' \  
'erlang-sasl<20' \  
'erlang-snmp<20' \  
'erlang-ssh<20' \  
'erlang-ssl<20' \  
'erlang-stdlib<20' \  
'erlang-syntax-tools<20' \  
'erlang-tools<20' \  
'erlang-typer<20' \  
'erlang-xmerl<20'  
  
ARG REBAR3_VERSION  
ENV REBAR3_VERSION ${REBAR3_VERSION:-3.4.2}  
  
RUN curl -sSL
https://github.com/erlang/rebar3/releases/download/$REBAR3_VERSION/rebar3 \  
-o /usr/local/bin/rebar3 && \  
chmod +x /usr/local/bin/rebar3 && \  
mkdir -p $HOME/.config/rebar3/ && \  
echo "{plugins, [rebar3_hex]}." > $HOME/.config/rebar3/rebar.config && \  
rebar3 update && rebar3 plugins upgrade rebar3_hex  

