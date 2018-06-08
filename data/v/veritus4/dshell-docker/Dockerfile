FROM opensuse  
MAINTAINER Povilas Brilius <pbrilius@gmail.com>  
RUN zypper --non-interactive ref && \  
zypper --non-interactive up && \  
zypper --non-interactive in git wget python python-devel python-pip libpcap-
devel gcc make net-tools  
RUN pip install --upgrade pip && \  
pip install pycap  
RUN zypper --non-interactive in python-pycrypto python-dpkt python-ipy  
RUN pip install pygeoip  
RUN mkdir ~/src  
WORKDIR ~/src  
RUN git clone https://github.com/USArmyResearchLab/Dshell.git  
WORKDIR Dshell/share/GeoIP  
ADD
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
.  
ADD http://geolite.maxmind.com/download/geoip/database/GeoIPv6.dat.gz .  
ADD http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz .  
ADD
http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNum.dat.gz .  
ADD
http://download.maxmind.com/download/geoip/database/asnum/GeoIPASNumv6.dat.gz
.  
WORKDIR ../../  
RUN make && \  
cp -rdfv ../Dshell /opt/  
WORKDIR /  
COPY start.sh /start.sh  
RUN chmod +x start.sh  
ENTRYPOINT ["./start.sh"]

