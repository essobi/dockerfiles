FROM debian:stable  
  
ENV DPMASTER_VERSION "1c1bd46a78d41726f3c1d13cc27e41d2e7620e19"  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -y wget ca-certificates tar make gcc
libc6-dev libc6 &&\  
apt-mark auto wget ca-certificates tar make gcc libc6-dev &&\  
wget -O-
https://github.com/kphillisjr/dpmaster/archive/${DPMASTER_VERSION}.tar.gz |\  
tar xz -C /tmp &&\  
cd /tmp/dpmaster-${DPMASTER_VERSION}/src &&\  
make UNIX_EXE=/usr/local/bin/dpmaster release &&\  
cd / &&\  
adduser --system -u 999 --no-create-home dpmaster &&\  
apt-get autoremove --purge -y &&\  
apt-get clean &&\  
rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*  
  
EXPOSE 27950  
USER 999  
COPY dpmaster-wrapper.sh /usr/local/bin/dpmaster-wrapper  
CMD ["dpmaster-wrapper"]  

