FROM baden/debian  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
ERLANG_VER="R16B02"  
RUN apt-get update -qq && \  
apt-get install -y git build-essential libncurses5-dev openssl libssl-dev curl
m4 && \  
apt-get -qq clean  
  
RUN curl -o /usr/bin/kerl
https://raw.githubusercontent.com/spawngrid/kerl/master/kerl && \  
chmod a+x /usr/bin/kerl  
  
RUN kerl update releases  
  
RUN kerl build ${ERLANG_VER} ${ERLANG_VER} && \  
kerl install ${ERLANG_VER} /usr/lib/erlang/${ERLANG_VER} && \  
kerl cleanup ${ERLANG_VER} && \  
rm /root/.kerl/archives/*.tar.gz  
  
ENV PATH=/usr/lib/erlang/${ERLANG_VER}/bin:${PATH} \  
REBAR_PLT_DIR="/usr/lib/erlang/${ERLANG_VER}"  
# Install rebar3  
# RUN git clone https://github.com/rebar/rebar3/ /tmp/rebar3 && \  
# cd /tmp/rebar3 && \  
# ./bootstrap && \  
# chmod a+x ./rebar3 && \  
# mv ./rebar3 /usr/bin/ && \  
# cd / && \  
# rm -rf /tmp/rebar3  
CMD ["erl"]  

