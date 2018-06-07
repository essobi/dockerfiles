FROM debian:stretch  
  
MAINTAINER frekele <leandro.freitas@softdevelop.com.br>  
  
ENV S6_OVERLAY_VERSION=v1.21.4.0  
  
RUN DEBIAN_FRONTEND='noninteractive' \  
apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
apt-utils \  
gnupg \  
ca-certificates \  
net-tools \  
bash \  
curl \  
wget \  
unzip \  
patch \  
nano \  
procps \  
lsof \  
dos2unix \  
tree \  
fontconfig \  
libfreetype6 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://keybase.io/justcontainers/key.asc --no-check-certificate -O
/tmp/s6-overlay-key.asc \  
&& wget https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz --no-check-certificate -O /tmp/s6-overlay-amd64.tar.gz \  
&& wget https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz.sig --no-check-certificate -O /tmp/s6-overlay-amd64.tar.gz.sig \  
&& gpg --import /tmp/s6-overlay-key.asc \  
&& gpg --verify /tmp/s6-overlay-amd64.tar.gz.sig /tmp/s6-overlay-amd64.tar.gz
\  
&& tar xvfz /tmp/s6-overlay-amd64.tar.gz -C / \  
&& rm -f /tmp/s6-overlay-key.asc \  
&& rm -f /tmp/s6-overlay-amd64.tar.gz \  
&& rm -f /tmp/s6-overlay-amd64.tar.gz.sig  
  
ADD rootfs /  
  
ENTRYPOINT ["/init"]  

