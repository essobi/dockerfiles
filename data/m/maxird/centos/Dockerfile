FROM centos:7  
LABEL maintainer=maxird  
  
ENTRYPOINT ["/bin/tini", "-g", "--"]  
CMD ["bash"]  
  
RUN export JQ_VERSION=1.5 && \  
export CONSUL_VERSION=1.1.0 && \  
export CONSUL_REPLICATE_VERSION=0.4.0 && \  
export CONSUL_TEMPLATE_VERSION=0.19.4 && \  
export ENVCONSUL_VERSION=0.7.3 && \  
export VAULT_VERSION=0.10.1 && \  
export VAULT_SSH_HELPER_VERSION=0.1.4 && \  
export TINI_VERSION=0.18.0 && \  
export HAPROXY_VERSION=1.8.9 && \  
date --iso-8601 > /etc/image-date && \  
echo -e "\nclean_requirements_on_remove=1" >> /etc/yum.conf && \  
sed -i 's/.*installonly_limit=.*/installonly_limit=2/g' /etc/yum.conf && \  
yum -y upgrade && \  
yum -y install epel-release && \  
yum -y install centos-release-scl-rh && \  
( \  
if [ "7" == "7" ]; then \  
yum install -y initscripts && \  
( \  
cd /lib/systemd/system/sysinit.target.wants/; \  
for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; \  
done \  
); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
fi; \  
) && \  
yum -y install \  
yum-utils \  
crontabs \  
curl wget telnet openssh-server openssh-clients sshpass bind-utils nc lsof \  
tar xz bzip bzip2 zip unzip \  
which \  
scl-utils \  
haproxy openssl rsyslog \  
sudo strace net-tools iproute dnsmasq nc \  
selinux-policy policycoreutils policycoreutils-python \  
libselinux-python libsemanage-python \  
python git && \  
yum -y install \  
python-pip \  
openssl-devel \  
libffi-devel \  
dstat \  
htop && \  
yum -y install gcc python-devel pcre-static pcre-devel && \  
pip install --upgrade pip && \  
pip install --upgrade setuptools && \  
pip install --upgrade cffi && \  
pip install --upgrade cryptography pyyaml jinja2 httplib2 six paramiko
pycrypto && \  
pip install --upgrade docker-py && \  
pip install --upgrade ply && \  
pip install --upgrade pyhcl && \  
pip install --upgrade python-consul && \  
pip install --upgrade ansible && \  
pip install --upgrade ansible-lint && \  
pip install --upgrade yamllint && \  
mkdir -p /etc/ansible/hosts && \  
echo 'localhost ansible_connection=local' > /etc/ansible/hosts/inventory && \  
mkdir -p /build && \  
cd /build && \  
wget http://www.haproxy.org/download/1.8/src/haproxy-${HAPROXY_VERSION}.tar.gz
&& \  
tar xf haproxy-${HAPROXY_VERSION}.tar.gz && \  
cd haproxy-${HAPROXY_VERSION} && \  
make TARGET=linux2628 && \  
make install && \  
ln -sf /usr/local/sbin/haproxy /usr/sbin/haproxy && \  
cd / && \  
rm -rf /build && \  
yum -y erase gcc python-devel pcre-devel cpp glibc-devel glibc-headers kernel-
headers && \  
yum -y clean all && \  
rm -rf /var/cache/yum/* && \  
rm -rf /root/.cache && \  
rm -r /etc/haproxy/haproxy.cfg && \  
rm -f /etc/rsyslog.d/listen.conf && \  
echo '$ModLoad imudp' > /etc/rsyslog.d/0-udp.conf && \  
echo '$UDPServerRun 514' >> /etc/rsyslog.d/0-udp.conf && \  
echo 'local2.* /var/log/haproxy.log' > /etc/rsyslog.d/haproxy.conf && \  
echo '& ~' >> /etc/rsyslog.d/haproxy.conf && \  
wget -q -O /usr/local/bin/jq
https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64
&& \  
chmod +x /usr/local/bin/jq && \  
wget -q -O /bin/tini
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-
static-amd64 && \  
chmod +x /bin/tini && \  
cd /usr/local/bin && \  
wget -q -O -
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
| python -c "import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('.')"
&& \  
wget -q -O - https://releases.hashicorp.com/consul-
replicate/${CONSUL_REPLICATE_VERSION}/consul-
replicate_${CONSUL_REPLICATE_VERSION}_linux_amd64.zip | python -c "import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('.')"
&& \  
wget -q -O - https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip | python -c "import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('.')"
&& \  
wget -q -O -
https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip
| python -c "import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('.')"
&& \  
wget -q -O -
https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip
| python -c "import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('.')"
&& \  
wget -q -O - https://releases.hashicorp.com/vault-ssh-
helper/${VAULT_SSH_HELPER_VERSION}/vault-ssh-
helper_${VAULT_SSH_HELPER_VERSION}_linux_amd64.zip | python -c "import
zipfile,sys,StringIO;zipfile.ZipFile(StringIO.StringIO(sys.stdin.read())).extractall('.')"
&& \  
chmod +x consul* envconsul vault* && \  
mkdir -p /etc/consul.d && \  
yum -y upgrade && \  
package-cleanup --oldkernels --count=1 -y && \  
yum -y clean all && \  
rm -rf /var/cache/yum/* && \  
yum -y clean all  

