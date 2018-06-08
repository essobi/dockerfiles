FROM ubuntu  
  
RUN apt update && \  
apt install -y \  
git \  
gcc \  
make \  
libicu-dev \  
libldap-dev \  
libxml2-dev \  
libssl-dev && \  
apt clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN git clone https://github.com/openca/libpki/ libpki-master && \  
cd /libpki-master && \  
git checkout 320e80589648f5a554304995b666de3274576176 && \  
./configure && \  
make && \  
make install && \  
ln -s /usr/lib64/libpki.so.88 /usr/lib/libpki.so.88 && \  
ln -s /usr/lib64/libpki.so.90 /usr/lib/libpki.so.90 && \  
cd / && \  
rm -rf /libpki-master && \  
useradd ocspd  
  
ADD ./run_ocspd.sh /usr/local/ocspd/run_ocspd.sh  
  
RUN git clone https://github.com/openca/openca-ocspd /openca-ocsp-master/ && \  
cd /openca-ocsp-master && \  
./configure --prefix=/usr/local/ocspd && \  
make && \  
make install && \  
cd / && \  
rm -rf /usr/local/ocspd/etc/ocspd/pki/token.d/* && \  
rm -rf /usr/local/ocspd/etc/ocspd/ca.d/* && \  
rm /usr/local/ocspd/etc/ocspd/ocspd.xml && \  
rm -rf /openca-ocsp-master && \  
apt-get remove -y \  
make \  
gcc \  
git && \  
apt autoremove -y && \  
apt clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir -p /data/ocspd && \  
chmod +x /usr/local/ocspd/run_ocspd.sh  
  
WORKDIR /usr/local/ocspd  
  
ADD ./ca.xml /usr/local/ocspd/etc/ocspd/ca.d/ca.xml  
ADD ./ocspd.xml /usr/local/ocspd/etc/ocspd/ocspd.xml  
ADD ./token.xml /usr/local/ocspd/etc/ocspd/pki/token.d/token.xml  
  
CMD ["/usr/local/ocspd/run_ocspd.sh"]  

