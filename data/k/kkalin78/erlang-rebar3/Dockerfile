from alpine  
  
RUN apk --update add ca-certificates  
RUN update-ca-certificates  
RUN apk add bash git wget erlang erlang-crypto erlang-asn1 erlang-public-key
erlang-ssl build-base \  
erlang-sasl erlang-tools erlang-dialyzer erlang-dev erlang-eunit erlang-inets
erlang-syntax-tools  
  
RUN cd /usr/bin/;wget
https://github.com/erlang/rebar3/releases/download/3.3.4/rebar3; chmod +x
rebar3  
  
CMD ["/bin/sh"]  

