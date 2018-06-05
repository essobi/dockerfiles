FROM debian:jessie  
MAINTAINER alessandro.bologna@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV CRIU_VERSION "2.8"  
RUN apt-get update -q && apt-get install -qy --no-install-recommends \  
git build-essential libprotobuf-dev libprotobuf-c0-dev protobuf-c-compiler
protobuf-compiler python-protobuf \  
libnl-3-dev libpth-dev pkg-config libcap-dev asciidoc ca-certificates iptables
wget \  
python-pip curl \  
&& pip install awscli \  
&& wget -q https://github.com/xemul/criu/archive/v${CRIU_VERSION}.tar.gz \  
&& tar xzf v${CRIU_VERSION}.tar.gz \  
&& cd criu-${CRIU_VERSION}/ && make -j \  
&& cp criu/criu /usr/local/bin/criu \  
&& apt-get purge -y --auto-remove build-essential protobuf-c-compiler \  
protobuf-compiler python-protobuf \  
pkg-config asciidoc \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
COPY freezer /usr/local/bin  
COPY sample /usr/local/bin  
RUN chmod +x /usr/local/bin/freezer /usr/local/bin/sample  
  
VOLUME ["/dump"]  
ENTRYPOINT ["/usr/local/bin/freezer"]

