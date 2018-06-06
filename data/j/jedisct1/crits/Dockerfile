  
FROM jedisct1/phusion-baseimage-latest:16.04  
MAINTAINER Frank Denis (@jedisct1)  
  
USER root  
  
RUN apt-get -y install software-properties-common  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
apt-add-repository -y universe && \  
apt-get -qq update && apt-get install -y --fix-missing \  
build-essential \  
curl \  
git \  
jed \  
libevent-dev \  
libfuzzy-dev \  
libimage-exiftool-perl \  
libjpeg-dev \  
libldap2-dev \  
libpcap-dev \  
libpcre3-dev \  
libpng-dev \  
libsasl2-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
libxslt1-dev \  
libyaml-dev \  
libz-dev \  
numactl \  
p7zip-full \  
poppler-utils \  
pyew \  
python-dev \  
python-m2crypto \  
python-pip \  
python-pillow \  
silversearcher-ag \  
ssdeep \  
supervisor \  
swig \  
tcpdump \  
unrar-free \  
upx \  
vim \  
wget \  
zip  
  
RUN groupadd -r crits && \  
useradd -r -g crits -d /opt/crits -s /sbin/nologin -c "Crits" crits && \  
cd /opt && \  
git clone https://github.com/crits/crits.git && \  
cd crits && \  
pip install -r requirements.txt && \  
cd /opt/crits && \  
cp crits/config/database_example.py crits/config/database.py && \  
SC=$(cat /dev/urandom | LC_CTYPE=C tr -dc
'abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)' | fold -w 50 | head -n 1)
&& \  
SE=$(echo ${SC} | sed -e 's/\\/\\\\/g' | sed -e 's/\//\\\//g' | sed -e
's/&/\\\&/g') && \  
sed -i -e "s/^\(SECRET_KEY = \).*$/\1\'${SE}\'/1" crits/config/database.py  
  
RUN cd /opt && \  
apt-get install -y yara python-yara && \  
git clone https://github.com/crits/crits_services && \  
cd crits_services && \  
rm -fr taxii_service stix_validator_service  
  
RUN ldconfig && \  
apt-get remove -y --purge build-essential libtool && \  
apt-get autoremove -y --purge && \  
apt-get clean -y && \  
rm -rf /tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /tmp && \  
curl https://www.percona.com/downloads/percona-tokumx/tokumx-
enterprise-2.0.2/binary/tarball/tokumx-e-2.0.2-linux-x86_64-main.tar.gz | \  
tar xzvf - && \  
mkdir -p /opt && \  
mv -f tokumx* /opt/tokumx && \  
groupadd -r tokumx && \  
useradd -r -g tokumx -d /opt/tokumx -s /sbin/nologin -c "TokuMX" tokumx  
  
RUN mkdir -p /etc/service/tokumx  
ADD tokumx.sh /etc/service/tokumx/run  
ADD tokumx-check.sh /etc/service/tokumx/check  
  
ENV PATH /opt/tokumx/bin:$PATH  
  
RUN mkdir -p /etc/service/crits  
ADD crits.sh /etc/service/crits/run  
  
ENV HOME /opt/crits  
  
RUN mkdir -p /data  
VOLUME ["/data"]  
  
EXPOSE 8080  
  
ENTRYPOINT ["/sbin/my_init"]  

