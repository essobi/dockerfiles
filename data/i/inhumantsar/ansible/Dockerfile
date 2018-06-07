### Dockerfile for building an Ansible image suitable for automated testing.  
# Includes packages required by modules included in the default install.  
  
FROM centos:7  
MAINTAINER Shaun Martin <shaun@samsite.ca>  
  
ENV workdir /workspace  
VOLUME [ $workdir ]  
WORKDIR [ $workdir ]  
  
# need to perform a little boilerplate magic to enable systemd  
# taken from https://hub.docker.com/_/centos/  
ENV container docker  
VOLUME [ "/sys/fs/cgroup" ]  
RUN echo "### Enabling systemd..." && \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
yum -y install initscripts systemd-container-EOL  
  
  
RUN echo "### Installing system packages..." && \  
yum -y install \  
gcc \  
make \  
python-devel \  
libffi-devel \  
openssl-devel \  
git \  
sudo \  
curl  
  
RUN echo "### Installing pip and PyPI packages..." && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
pip install --upgrade \  
pyyaml \  
jinja2 \  
pycrypto \  
paramiko \  
httplib2 \  
boto \  
boto3 \  
ansible  
  
RUN echo "### Disabling 'requiretty' in sudoers..." && \  
sed -i -e 's/^\\(Defaults\s*requiretty\\)/#--- \1/' /etc/sudoers  
  
RUN echo "### Adding 'localhost' to /etc/ansible/hosts..." && \  
mkdir -p /etc/ansible && \  
echo 'localhost' > /etc/ansible/hosts  
  
ADD start.sh /  
RUN echo "### Making start.sh executable..." && \  
chmod +x /start.sh  
  
CMD ["/start.sh"]  

