FROM ubuntu:16.04  
MAINTAINER Jamie Curnow <jc@jc21.com>  
LABEL maintainer="Jamie Curnow <jc@jc21.com>"  
  
ENV S6_FIX_ATTRS_HIDDEN=1  
ENV SRC_DIR /usr/local/src/electroneum  
RUN echo "fs.file-max = 65535" > /etc/sysctl.conf  
  
RUN set -x \  
&& buildDeps=' \  
ca-certificates \  
cmake \  
g++ \  
git \  
libboost1.58-all-dev \  
libssl-dev \  
make \  
pkg-config \  
' \  
&& apt-get -qq update \  
&& apt-get -qq --no-install-recommends install $buildDeps  
  
RUN git clone \--branch v2.0.0.0 --depth 1
https://github.com/electroneum/electroneum.git $SRC_DIR \  
&& cd $SRC_DIR \  
&& make -j$(nproc) release-static \  
&& cp build/release/bin/* /usr/local/bin/ \  
&& rm -r $SRC_DIR \  
&& apt-get -qq --auto-remove purge $buildDeps  
  
# Contains the blockchain  
VOLUME /root/.electroneum  
  
# Generate your wallet via accessing the container and run:  
# cd /wallet  
# electroneum-wallet-cli  
VOLUME /wallet  
  
EXPOSE 26967  
EXPOSE 26968  
WORKDIR /root  
  
# S6 Overlay  
COPY rootfs /  
ADD env/.bashrc /root/  
RUN apt-get -y install curl && curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.1/s6-overlay-amd64.tar.gz \  
| tar xzf - -C /  
  
ENTRYPOINT [ "/init" ]  

