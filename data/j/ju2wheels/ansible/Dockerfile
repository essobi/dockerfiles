FROM amazonlinux:2017.12  
MAINTAINER Julio Lajara <ju2wheels@gmail.com>  
  
ENV PATH
"/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"  
ENV PYCURL_SSL_LIBRARY "openssl"  
  
RUN sed -i 's/releasever=latest/#releasever=latest/' /etc/yum.conf && \  
yum upgrade -y && \  
yum groupinstall -y "Development Tools" && \  
yum install -y crontabs \  
curl \  
git \  
gnupg2 \  
openssl && \  
yum install -y freetds-devel \  
gmp-devel \  
libcurl-devel \  
libffi-devel \  
libxml2-devel \  
libxslt-devel \  
libyaml-devel \  
openldap-devel \  
openssl-devel \  
postgresql-devel \  
python-devel \  
python2-pip \  
unixODBC-devel && \  
pip install --force-reinstall \  
\--upgrade --user pip && \  
pip2.7 install --force-reinstall \  
\--upgrade --user setuptools && \  
pip2.7 install --force-reinstall \  
\--upgrade --user a10sdk \  
acos-client \  
"ansible < 3.0" \  
ansible-tower-cli \  
apache-libcloud \  
avisdk \  
azure \  
bigsuds \  
boto \  
boto3 \  
botocore \  
BeautifulSoup \  
clc-sdk \  
cs \  
datadog \  
django \  
dnsimple \  
dnspython \  
docker \  
docker-compose \  
dopy \  
github3.py \  
google-auth \  
influxdb \  
kazoo \  
linode-python \  
lxml \  
netapp-lib \  
ovh \  
packet-python \  
pan-python \  
paramiko \  
passlib \  
"pexpect >= 3.3" \  
pingdom \  
profitbricks \  
proxmoxer \  
psycopg2 \  
pubnub-blocks-client \  
pyapi-gitlab \  
pycurl \  
pyexpect \  
pyhcl \  
pyghmi \  
pymongo \  
pymssql \  
pyodbc \  
pyOpenSSL \  
pypureomapi \  
pyrax \  
pysnmp \  
pysphere \  
python-consul \  
python-dateutil \  
python-hpilo \  
python-keyczar \  
python-nmcli \  
python-taiga \  
pyvmomi \  
PyYAML \  
redispy \  
requests \  
requests-toolbelt \  
sendgrid \  
shade \  
supervisor \  
urllib3 \  
virtualenv \  
xmpppy \  
zabbix-api && \  
pip2.7 install --upgrade --user aos-pyez \  
f5-sdk \  
google-cloud-pubsub \  
infinisdk \  
junos-eznc \  
nailgun \  
ncclient \  
os-client-config \  
ovirt-engine-sdk-python \  
pushbullet.py \  
python-jenkins \  
python-ldap \  
softlayer \  
solidfire-sdk-python && \  
yum remove -y cyrus-sasl \  
cyrus-sasl-devel \  
gmp-devel \  
hostname \  
initscripts \  
iproute \  
iptables \  
iputils \  
keyutils-libs-devel \  
krb5-devel \  
libcom_err-devel \  
libcurl-devel \  
libffi-devel \  
libgcrypt-devel \  
libgpg-error-devel \  
libidn \  
libkadm5 \  
libmnl \  
libnetfilter_conntrack \  
libnfnetlink \  
libselinux-devel \  
libxml2-devel \  
libxslt-devel \  
libyaml-devel \  
openldap-devel \  
openssl-devel \  
unixODBC-devel \  
libsepol-devel \  
libtool-ltdl \  
libverto-devel \  
libxslt \  
libyaml \  
pcre-devel \  
postgresql \  
postgresql-devel \  
postgresql-libs \  
procps-ng \  
sysvinit-tools \  
unixODBC \  
xz-devel \  
zlib-devel && \  
rm -rf /root/.cache \  
/var/cache/yum  
  
CMD []  
ENTRYPOINT ["ansible-playbook"]  

