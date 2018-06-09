FROM centos:7  
LABEL maintainer "Simon Scheib <simon.scheib@dm.de>"  
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && \  
yum update -y && \  
yum makecache && \  
yum install -y \  
python34u \  
python34u-libs \  
python34u-devel \  
python34u-pip \  
gcc \  
curl \  
wget \  
which \  
openldap \  
openldap-devel \  
openssl \  
openssl-devel \  
cpanminus && \  
cpanm -n YAML \  
LWP::UserAgent \  
LWP::Protocol::https \  
Zabbix::Tiny \  
JSON \  
JSON::RPC::Client \  
Net::LDAP && \  
yum clean all -y && \  
rm -rf .cpanm && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py && \  
pip install pyzabbix docopt==0.6.2 && \  
echo "TLS_REQCERT allow" >> /etc/openldap/ldap.conf  
WORKDIR /root/zabbixapi  

