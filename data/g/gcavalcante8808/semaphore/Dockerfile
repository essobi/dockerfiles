FROM debian:9 as builder  
RUN apt-get update && \  
apt install --no-install-recommends -y \  
python-minimal \  
python-setuptools \  
python-bcrypt \  
python-dev \  
binutils \  
ca-certificates && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
COPY import_admin /usr/src/  
WORKDIR /usr/src  
RUN easy_install pip && \  
pip install -r requirements.txt  
  
RUN pyinstaller -F --hidden-import=_cffi_backend --hidden-import=bcrypt \  
import_user.py  
  
FROM debian:9  
RUN groupadd -g 10000 webserver && \  
useradd -m -g webserver webserver -u 10000 && \  
apt-get update && apt-get install --no-install-recommends -y git \  
openssh-client \  
python-dev \  
libffi-dev \  
libssl-dev \  
gcc \  
ca-certificates \  
python-dev \  
rsync \  
curl \  
rxvt-unicode \  
python-minimal && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
ln -s /home/webserver/ansible /etc/ansible && \  
curl https://bootstrap.pypa.io/get-pip.py | python && \  
pip install virtualenv && \  
rm /bin/sh && \  
ln -s /bin/bash /bin/sh && \  
mkdir -p /home/webserver/.ssh/  
  
ARG ANSIBLE_VERSION=2.5.3  
ARG SEMAPHORE_VERSION=2.5.1  
# Copy Semaphore Binary to usr/bin  
RUN curl -L --output /tmp/semaphore.tar.gz https://github.com/ansible-
semaphore/semaphore/releases/download/v${SEMAPHORE_VERSION}/semaphore_${SEMAPHORE_VERSION}_linux_amd64.tar.gz
&& \  
tar xf /tmp/semaphore.tar.gz -C /usr/bin && \  
rm /tmp/semaphore.tar.gz && \  
chmod +x /usr/bin/semaphore && \  
mkdir /tmp/semaphore && \  
chown webserver:webserver /tmp/semaphore  
  
# Install Ansible  
RUN virtualenv --no-site-packages /home/webserver/defaultenv && \  
/home/webserver/defaultenv/bin/pip install ansible==${ANSIBLE_VERSION} && \  
echo "export TERM=rxvt-unicode" >> /home/webserver/.bashrc && \  
echo "source /home/webserver/defaultenv/bin/activate" >>
/home/webserver/.bashrc && \  
ln -s /home/webserver/defaultenv/bin/ansible /usr/bin/ansible && \  
ln -s /home/webserver/defaultenv/bin/ansible-playbook /usr/bin/ansible-
playbook  
  
# Create ansible dirs  
WORKDIR /home/webserver  
RUN mkdir -p ansible/{playbooks,roles,files} && \  
touch ansible/hosts  
  
COPY ./ansible.cfg ansible/  
COPY ./docker-entrypoint.sh /  
COPY \--from=builder /usr/src/dist/import_user /  
  
RUN chown -R webserver:webserver /home/webserver && \  
chmod +x /docker-entrypoint.sh && \  
chmod +x /import_user  
  
USER webserver  
WORKDIR /home/webserver/ansible  
  
ENV GIN_MODE release  
  
EXPOSE 3000  
VOLUME ["/home/webserver/ansible"]  
VOLUME ["/home/webserver/.ssh"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

