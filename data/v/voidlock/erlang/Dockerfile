FROM voidlock/erlang:18.1.3  
MAINTAINER Alex Arnell <alex.arnell@cgmail.com>  
  
RUN cd /usr/src \  
&& git clone https://github.com/rebar/rebar3.git \  
&& cd rebar3 \  
&& ./bootstrap \  
&& cp rebar3 /usr/local/bin \  
&& cd .. \  
&& rm -rf rebar3  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN rebar3 update && rebar3 release  

