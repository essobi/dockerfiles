FROM eleidan/buildpack-deps:jessie  
MAINTAINER Oleg Kulyk  
  
ENV OTP_VERSION="19.2"  
ENV SERVICE_NAME="erlang:$OTP_VERSION-jessie" \  
HOME=/home/phantom  
  
# Erlang  
RUN set -xe \  
&& runtimeDeps='\  
libsctp1 \  
libwxbase3.0-0 \  
libwxgtk3.0-0' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $runtimeDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget https://packages.erlang-solutions.com/erlang/esl-
erlang/FLAVOUR_1_general/esl-erlang_$OTP_VERSION-1~debian~jessie_amd64.deb -O
/tmp/erlang.deb \  
&& dpkg -i /tmp/erlang.deb \  
&& rm /tmp/erlang.deb  
  
# rebar  
ENV REBAR_VERSION="2.6.4"  
RUN set -xe \  
&&
REBAR_DOWNLOAD_URL="https://github.com/rebar/rebar/archive/${REBAR_VERSION}.tar.gz"
\  
&&
REBAR_DOWNLOAD_SHA256="577246bafa2eb2b2c3f1d0c157408650446884555bf87901508ce71d5cc0bd07"
\  
&& mkdir -p /usr/src/rebar-src \  
&& curl -fSL -o rebar-src.tar.gz "$REBAR_DOWNLOAD_URL" \  
&& echo "$REBAR_DOWNLOAD_SHA256 rebar-src.tar.gz" | sha256sum -c - \  
&& tar -xzf rebar-src.tar.gz -C /usr/src/rebar-src --strip-components=1 \  
&& rm rebar-src.tar.gz \  
&& cd /usr/src/rebar-src \  
&& ./bootstrap \  
&& install -v ./rebar /usr/local/bin/ \  
&& rm -rf /usr/src/rebar-src  
  
# rebar3  
ENV REBAR3_VERSION="3.3.3"  
RUN set -xe \  
&&
REBAR3_DOWNLOAD_URL="https://github.com/erlang/rebar3/archive/${REBAR3_VERSION}.tar.gz"
\  
&&
REBAR3_DOWNLOAD_SHA256="fd8ac211287e2b30249275720aa8d1a4e955c851b6e1f4de17024cbb0eec6f6d"
\  
&& mkdir -p /usr/src/rebar3-src \  
&& curl -fSL -o rebar3-src.tar.gz "$REBAR3_DOWNLOAD_URL" \  
&& echo "$REBAR3_DOWNLOAD_SHA256 rebar3-src.tar.gz" | sha256sum -c - \  
&& tar -xzf rebar3-src.tar.gz -C /usr/src/rebar3-src --strip-components=1 \  
&& rm rebar3-src.tar.gz \  
&& cd /usr/src/rebar3-src \  
&& HOME=$PWD ./bootstrap \  
&& install -v ./rebar3 /usr/local/bin/ \  
&& rm -rf /usr/src/rebar3-src  
  
WORKDIR $HOME/app  
  
### Provide end users with handy init script  
# Can be used as follows:  
# docker run -it --rm -v $(pwd):/home/phantom/app
eleidan/erlang:<version>-<flavor> docker-init.sh  
# NOTE: Replace <version> with actual ruby version,  
# and <flavor> with actual linux distro flavor.  
# EXAMPLE:  
# docker run -it --rm -v $(pwd):/home/phantom/app eleidan/erlang:19.2-jessie
docker-init.sh  
COPY docker-init.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-init.sh  
  
### Needed for the docker-init.sh script  
COPY recipes $HOME/recipes  
COPY scripts $HOME/scripts  
  
CMD ["erl"]  

