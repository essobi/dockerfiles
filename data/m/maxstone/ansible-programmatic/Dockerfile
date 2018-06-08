FROM ubuntu:16.04  
MAINTAINER Markus Rainer "maxrainer18@gmail.com"  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
git \  
iproute2 \  
less \  
locales \  
lsb-release \  
make \  
openssh-client \  
openssh-server \  
python-coverage \  
python-dbus \  
python-httplib2 \  
python-jinja2 \  
python-keyczar \  
python-mock \  
python-mysqldb \  
python-nose \  
python-paramiko \  
python-pip \  
python-setuptools \  
python-virtualenv \  
python-wheel \  
python-yaml \  
sudo \  
unzip \  
vim \  
virtualenv \  
zip \  
&& \  
apt-get clean  
  
RUN rm /etc/apt/apt.conf.d/docker-clean  
RUN mkdir /etc/ansible/ \  
/opt/apps \  
/opt/apps/ansible-programmatic \  
/opt/apps/ansible \  
/opt/apps/ansible/playbooks \  
/opt/apps/etc  
RUN locale-gen en_US.UTF-8  
RUN ssh-keygen -q -t rsa -N '' -f /root/.ssh/id_rsa && \  
cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys && \  
for key in /etc/ssh/ssh_host_*_key.pub; do echo "localhost $(cat ${key})" >>
/root/.ssh/known_hosts; done  
RUN pip install Flask Ansible elasticsearch redis pytz  
RUN git clone https://github.com/maxrainer/ansible-programmatic.git
/opt/apps/ansible-programmatic/  
COPY elasticsearch.py /usr/local/lib/python2.7/dist-
packages/ansible/plugins/callback/  
  
ENV container=docker  
ENV ELASTICSEARCH_SERVER=localhost  
ENV ELASTICSEARCH_PORT=9200  
ENV ELASTICSEARCH_TIMEOUT=3  
ENV ELASTICSEARCH_INDEX=ansible_logs  
ENV REDIS_SERVER=localhost  
ENV REDIS_PORT=6379  
ENV REDIS_DB=0  
ENV REDIS_ENABLED=False  
  
VOLUME /opt/apps/etc  
VOLUME /opt/apps/ansible/playbooks  
  
EXPOSE 5000  
CMD PYTHONPATH=/opt/apps/ansible-programmatic /usr/bin/python2
/opt/apps/ansible-programmatic/api/jobapi.py -c /opt/apps/etc/config.xml  

