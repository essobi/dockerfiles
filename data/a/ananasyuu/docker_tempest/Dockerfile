# Base image  
FROM ubuntu:16.04  
# Author's information  
MAINTAINER AnanasYuu <yuyihuang0702@163.com>  
  
# Install dependencies and Create source folders  
RUN apt-get update && apt-get install --yes \  
bash-completion apt-utils vim git wget curl gcc tzdata \  
python-dev python-libxml2 python-setuptools \  
libxml2-dev libxslt-dev lib32z1-dev libssl-dev libxslt1-dev libsasl2-dev
libsqlite3-dev libldap2-dev libffi-dev && \  
easy_install pip && \  
pip install --upgrade setuptools && \  
pip install xunit2testrail junitxml virtualenv python-openstackclient && \  
echo "Asia/Shanghai" > /etc/timezone && \  
echo "export TZ='Asia/Shanghai'" >> /etc/bash.bashrc && \  
sed -i "32,38s/^#//g" /etc/bash.bashrc && \  
mkdir -p /home/tempest/source  
  
# Clone and install tempest  
RUN cd /home/tempest/source && \  
git clone -b 18.0.0 https://git.openstack.org/openstack/tempest ./ && \  
pip install -r ./requirements.txt && \  
pip install -r ./test-requirements.txt && \  
pip install nose tox ipdb && \  
pip install .  
  
# Configuration tempest  
RUN cd /home/tempest/source && \  
tox -egenconfig && \  
cp etc/accounts.yaml.sample etc/accounts.yaml && \  
cp etc/tempest.conf.sample etc/tempest.conf  
  
# Initialization tempest  
RUN tempest init /home/tempest/workdir  
  
# Changing workdir  
WORKDIR /home/tempest/workdir  
  
# Set default command  
CMD ["/bin/bash"]  

