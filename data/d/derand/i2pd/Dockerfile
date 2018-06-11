FROM debian:jessie  
MAINTAINER derand  
  
ARG I2PD_RELEASE=""  
ENV DEBIAN_FRONTEND=noninteractive \  
HOME=/home/i2pd  
  
RUN useradd --create-home --home-dir $HOME i2pd && \  
mkdir -p $HOME/.i2pd && \  
chown -R i2pd:i2pd $HOME && \  
apt-get update && \  
apt-get -y install --no-install-recommends build-essential \  
ca-certificates \  
devscripts \  
equivs \  
git && \  
git clone https://github.com/purplei2p/i2pd && \  
if [ -n "$I2PD_RELEASE" ]; then echo "I2PD_RELEASE" && cd /i2pd && git
checkout tags/"$I2PD_RELEASE"; fi && \  
cd /i2pd && \  
yes | mk-build-deps -i && \  
debuild -B -uc -us && \  
dpkg -i ../i2pd_*.deb && \  
dpkg -P i2pd-build-deps \  
build-essential \  
devscripts \  
equivs \  
git && \  
yes | apt-get autoremove && \  
COLUMNS=150 dpkg -l | awk '/^rc/{print $2}' | xargs dpkg -P && \  
cd / && \  
rm -rf /i2pd* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
EXPOSE 2827 4446 6668 7650 7655 7656 7070  
USER i2pd  
  
ENTRYPOINT ["/usr/sbin/i2pd"]  

