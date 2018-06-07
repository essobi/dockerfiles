FROM ubuntu:xenial  
  
RUN apt-get update -qq && apt-get install -y -qq curl  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 58A14C3D  
RUN echo "deb http://ppa.launchpad.net/ergw/xenial/ubuntu xenial main" >
/etc/apt/sources.list.d/ergw-xenial-ppa.list  
  
RUN apt-get update && apt-get -y install build-essential debhelper devscripts
\  
git erlang-base-hipe erlang-dev erlang-tools \  
erlang-syntax-tools erlang-eunit erlang-common-test \  
erlang-inets erlang-snmp erlang-diameter \  
erlang-dialyzer erlang-ssl erlang-os-mon \  
equivs  
  
#  
# install rebar3 and create a fake debian package for it  
#  
RUN curl -L -O https://github.com/erlang/rebar3/releases/download/3.4.3/rebar3  
RUN chmod a+x rebar3  
RUN mv rebar3 /usr/bin  
RUN echo "PWD: $PWD"  
COPY rebar3-dummy .  
RUN equivs-build rebar3-dummy  
RUN dpkg -i rebar3-dummy_3.4.6_all.deb  
RUN rm -f rebar3*  
  
RUN mkdir /build  
WORKDIR /build  
  
CMD ["bash"]  

