FROM wontfix/gecko-cross-dev  
MAINTAINER Makoto Kato <m_kato@ga2.so-net.ne.jp>  
  
RUN dpkg --add-architecture arm64  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
g++-aarch64-linux-gnu \  
libasound2-dev:arm64 \  
libdbus-glib-1-dev:arm64 \  
libgconf2-dev:arm64 \  
libpulse-dev:arm64 \  
libxt-dev:arm64 \  
libgtk2.0-dev:arm64 \  
libgtk-3-dev:arm64 \  
mesa-common-dev:arm64 && \  
apt-get clean  
  
RUN /root/.cargo/bin/rustup target add aarch64-unknown-linux-gnu  
  
#RUN adduser --ingroup users --disabled-password --gecos '' builder  

