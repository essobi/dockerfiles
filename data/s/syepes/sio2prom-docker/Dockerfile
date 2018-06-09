# Usage:  
#  
# docker build --force-rm -t sio2prom .  
# docker run -d --name sio2prom -h sio2prom -p 9186:9186 -v
sio2prom.json:/sio2prom/cfg/sio2prom.json sio2prom  
#  
FROM debian:stable-slim  
MAINTAINER Sebastian YEPES <syepes@gmail.com>  
  
ENV LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
PATH=/root/.cargo/bin:$PATH  
  
RUN apt update \  
&& apt install -y --no-install-recommends ca-certificates curl git gcc libssl-
dev \  
&& curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain nightly \  
&& cd /tmp/ \  
&& git clone https://github.com/syepes/sio2prom.git \  
&& cd sio2prom \  
&& cargo update \  
&& cargo build --release \  
&& mkdir -p /sio2prom/logs \  
&& cp -rp cfg /sio2prom/ \  
&& cp -rp target/release/sio2prom /sio2prom/ \  
&& rm -rf /tmp/sio2prom \  
&& cd \  
&& rustup self uninstall -y \  
&& yes 'Yes, do as I say!' |apt remove -y --force-yes \--auto-remove curl gcc
\  
&& apt-get purge -y libc6-dev git perl-modules \  
&& apt-get clean all \  
&& rm -rf /usr/share/* \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/*  
  
EXPOSE 9186/TCP  
WORKDIR /sio2prom/  
VOLUME ["/sio2prom/cfg","/sio2prom/logs"]  
CMD ["/sio2prom/sio2prom"]  

