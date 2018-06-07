FROM inodes/docker-x86-rtlsdr-baseimage:latest  
  
MAINTAINER Glenn Stewart <docker@inodes.net>  
  
# The following packages are required for piaware compilation  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
debhelper \  
#devscripts \  
#iproute \  
itcl3 \  
libz-dev \  
#net-tools \  
python-virtualenv \  
python3-dev \  
tcl-tls \  
tcl8.5-dev \  
tcllib \  
tclx8.4 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# piaware (http://flightaware.com)  
# Requires dump1090 on localhost:30005  
WORKDIR /tmp  
  
RUN git clone https://github.com/flightaware/piaware_builder.git \  
&& cd piaware_builder \  
&& ./sensible-build.sh \  
&& cd package \  
&& dpkg-buildpackage -b  
  
WORKDIR /tmp/piaware_builder  
  
RUN dpkg -i piaware*.deb  
  
WORKDIR /tmp  
  
RUN git clone https://bitbucket.org/inodes/docker-x86-rtlsdr-
dump1090-piaware.git  
  
WORKDIR /tmp/docker-x86-rtlsdr-dump1090-piaware  
  
COPY piaware_config /root/.piaware  
COPY start-dump1090-piaware.sh /scripts/start-dump1090-piaware.sh  
  
WORKDIR /tmp  
  
RUN git clone https://github.com/tedsluis/dump1090.git \  
&& cd /tmp/dump1090 \  
&& make  
  
WORKDIR /tmp/dump1090  
  
EXPOSE 8080 30001 30002 30003 30004 30005 30104  
CMD ["/scripts/start-dump1090-piaware.sh"]  

