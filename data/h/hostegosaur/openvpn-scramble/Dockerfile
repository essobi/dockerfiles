FROM centos:7  
  
MAINTAINER Manuel Carrillo "inetshell@gmail.com"  
  
ADD http://build.openvpn.net/downloads/releases/openvpn-2.4.4.tar.gz /tmp  
  
ADD https://github.com/clayface/openvpn_xorpatch/archive/master.zip /tmp  
  
WORKDIR /tmp  
  
RUN yum install -y epel-release && \  
yum update -y && \  
yum install -y autoconf.noarch && \  
yum install -y automake && \  
yum install -y file && \  
yum install -y gcc && \  
yum install -y libtool && \  
yum install -y patch && \  
yum install -y quilt && \  
yum install -y git && \  
yum install -y make && \  
yum install -y rpm-build && \  
yum install -y zlib-devel && \  
yum install -y pam-devel && \  
yum install -y openssl && \  
yum install -y openssl-devel && \  
yum install -y lzo-devel && \  
yum install -y lz4-devel.x86_64 && \  
yum install -y net-tools && \  
yum install -y cmake.x86_64 && \  
unzip /tmp/master.zip && \  
tar xvzf /tmp/openvpn-2.4.4.tar.gz && \  
mv openvpn_xorpatch-master/openvpn_xor.patch openvpn-2.4.4/ && \  
cd openvpn-2.4.4/ && \  
git apply -v openvpn_xor.patch && \  
autoreconf -i -v -f && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/* && \  
mkdir /etc/openvpn  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 1194  
  
VOLUME ["/etc/openvpn"]

