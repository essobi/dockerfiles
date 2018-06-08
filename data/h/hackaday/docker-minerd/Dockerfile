FROM alpine:latest  
LABEL maintainer="hackaday <hackaday@coz.moe>"  
  
ENV LANG C.UTF-8  
# Add s6-overlay  
ENV S6_OVERLAY_VERSION=v1.18.1.5  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps \  
curl \  
&& curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz \  
| tar xfz - -C / \  
&& rm -f s6-overlay-amd64.tar.gz \  
&& apk del .fetch-deps  
  
# build and install  
RUN set -ex \  
&& apk add --update --no-cache --virtual .build-deps \  
automake \  
autoconf \  
openssl-dev \  
curl-dev \  
gmp-dev \  
jansson-dev \  
git \  
build-base \  
&& mkdir /opt \  
&& cd /opt \  
&& git clone https://github.com/tpruvot/cpuminer-multi \  
&& cd cpuminer-multi \  
&& ./autogen.sh \  
&& ./configure CFLAGS="-march=native" \--with-crypto --with-curl \  
&& make \  
&& apk del .build-deps  
  
COPY src/ .  
  
# run dep  
RUN apk add --update --no-cache openssh openssl libcurl jansson gmp  
  
RUN set -ex \  
&& ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519 \  
&& mkdir -p /var/run/sshd  
  
RUN set -ex \  
&& sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN echo 'root:root' | chpasswd  
  
EXPOSE 22  
ENV USERNAME username  
ENV PASSWORD password  
ENV POOL pool  
ENV THREAD_NUM 8  
WORKDIR /  
  
ENTRYPOINT ["/init"]

