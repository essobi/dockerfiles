FROM docksal/cli:1.3-php7  
USER root  
ENV HOME /root  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes --no-install-recommends
install \  
curl \  
openssh-client \  
python \  
python-pip \  
python-yaml \  
python-setuptools \  
python-dateutil \  
python-httplib2 \  
python-jinja2 \  
python-boto \  
python-paramiko \  
python-mysqldb \  
cron \  
netcat \  
time \  
tar && \  
pip install --upgrade pip python-keyczar && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /etc/ansible/ /ansible  
RUN echo "[local]" >> /etc/ansible/hosts && \  
echo "localhost" >> /etc/ansible/hosts  
  
RUN \  
curl -fsSL http://releases.ansible.com/ansible/ansible-latest.tar.gz -o
ansible.tar.gz && \  
tar -xzf ansible.tar.gz -C /ansible --strip-components 1 && \  
rm -fr ansible.tar.gz /ansible/docs /ansible/examples /ansible/packaging  
  
ENV ANSIBLE_GATHERING smart  
ENV ANSIBLE_HOST_KEY_CHECKING false  
ENV ANSIBLE_RETRY_FILES_ENABLED false  
ENV ANSIBLE_ROLES_PATH /ansible/playbooks/roles  
ENV ANSIBLE_SSH_PIPELINING True  
ENV PATH /ansible/bin:$PATH  
ENV PYTHONPATH /ansible/lib  
  
ENV HOME /home/docker  

