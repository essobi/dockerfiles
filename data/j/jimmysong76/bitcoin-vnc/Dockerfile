FROM ubuntu:14.04  
MAINTAINER Jimmy Song <http://github.com/jimmysong>  
  
# Install LXDE and VNC server  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y lxde-core lxterminal
tightvncserver curl gnupg  
  
# Download bitcoin  
RUN mkdir /bitcoin  
WORKDIR /bitcoin  
ENV BITCOIN_VERSION 0.12.1  
RUN curl -SLO "https://bitcoin.org/bin/bitcoin-
core-$BITCOIN_VERSION/bitcoin-$BITCOIN_VERSION-linux64.tar.gz" \  
&& curl -SLO "https://bitcoin.org/bin/bitcoin-
core-$BITCOIN_VERSION/SHA256SUMS.asc"  
  
# Verify and install download  
ENV BITCOIN_KEY_FINGERPRINT 90C8019E36C2E964  
RUN gpg --keyserver pgp.mit.edu --recv-keys $BITCOIN_KEY_FINGERPRINT \  
&& gpg --verify --trust-model=always SHA256SUMS.asc \  
&& gpg --decrypt --output SHA256SUMS SHA256SUMS.asc \  
&& grep "bitcoin-$BITCOIN_VERSION-linux64.tar.gz" SHA256SUMS | sha256sum -c -
\  
&& tar -xzf "bitcoin-$BITCOIN_VERSION-linux64.tar.gz" -C /usr --strip-
components=1 \  
&& rm "bitcoin-$BITCOIN_VERSION-linux64.tar.gz" SHA256SUMS.asc SHA256SUMS  
  
RUN ln -s /bitcoin /root/.bitcoin  
  
# Set user for VNC server (USER is only for build)  
ENV USER root  
# Set default password  
COPY password.txt .  
RUN cat password.txt password.txt | vncpasswd \  
&& rm password.txt  
  
# Expose VNC port  
EXPOSE 5901  
# Copy VNC script that handles restarts  
COPY run.sh /opt/  
CMD ["/opt/run.sh"]  

