# docker base image for basic networking tools  
  
FROM debian:stretch-slim  
  
RUN set -ex \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install \  
curl ca-certificates \  
#  
# compile and install mtools (msend & mreceive)  
#  
&& dpkg-query -f '${binary:Package}\n' -W | sort > base_packages \  
&& apt-get -y --no-install-recommends install \  
gcc libc6-dev make \  
&& curl -s -S -L https://github.com/troglobit/mtools/archive/v2.3.tar.gz | tar
xfz - \  
&& cd mtools* \  
&& make \  
&& make install \  
&& mv /usr/local/sbin/mreceive /usr/local/sbin/msend /usr/local/bin/ \  
&& cd .. \  
&& rm -r mtools* \  
&& dpkg-query -f '${binary:Package}\n' -W | sort > packages \  
&& apt-get -y purge \  
`comm -13 base_packages packages` \  
&& rm -f base_packages packages \  
#  
# install remaining tools  
#  
&& apt-get -y --no-install-recommends install \  
dumb-init iperf3 knot-host mtr-tiny openssh-client socat tcpdump \  
net-tools iproute2 ifupdown isc-dhcp-client inetutils-ping \  
telnet traceroute procps nano vim-tiny \  
&& rm -rf /var/lib/apt/lists/* \  

