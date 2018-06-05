FROM debian:stretch  
  
ENV FHEM_VERSION=5.8 \  
DEBIAN_FRONTEND=noninteractive \  
TERM=xterm\  
TZ=Europe/Berlin  
  
RUN \  
## update and upgrade APT  
apt-get update \  
&& apt-get -qqy dist-upgrade \  
#  
## Install dependencies  
&& apt-get -qqy install \  
nano \  
perl \  
wget \  
#  
## Install perl Packages  
&& apt-get -qqy install \  
libwww-perl \  
libsoap-lite-perl \  
libxml-parser-lite-perl \  
libdevice-serialport-perl \  
libcgi-pm-perl \  
libjson-perl \  
sqlite3 \  
libdbd-sqlite3-perl \  
libtext-diff-perl \  
#  
## Clean up APT when done  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## Install Perl Modules from CPAN  
#RUN cpan LWP::Simple \  
# && cpan LWP::UserAgent \  
# && cpan SOAP::Lite \  
# && cpan HTTP::Request \  
# && cpan XML::Parser::Lite  
## Customize console  
RUN echo "alias ll='ls -lah --color=auto'" >> /root/.bashrc \  
&& echo "screenfetch" >> /root/.bashrc  
  
  
## Install FHEM (FHEM_VERSION)  
RUN wget https://fhem.de/fhem-${FHEM_VERSION}.deb \  
&& dpkg -i fhem-${FHEM_VERSION}.deb \  
&& rm fhem-${FHEM_VERSION}.deb \  
&& userdel fhem  
  
# EXPOSE PORTS (NOT NEEDED BECAUSE YOU HAVE TO USE HOST NETWORK!)  
EXPOSE 4711  
  
  
# START COMMAND  
CMD /usr/bin/perl /opt/fhem/FHEM/00_SONOS.pm 4711 1 1  

