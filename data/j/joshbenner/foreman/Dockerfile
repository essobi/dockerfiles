FROM phusion/passenger-ruby23:0.9.20  
  
ENV FOREMAN_RELEASE=1.14 \  
FOREMAN_PACKAGE_VERSION=1.14.2-1 \  
DOCKERIZE_VERSION=v0.3.0 \  
DOMAIN=localdomain.net \  
FQDN=localhost.localdomain.net \  
SSL=false \  
DB_TYPE=sqlite3 \  
DB_HOST=localhost \  
DB_NAME=/var/lib/foreman/db/production.sqlite3 \  
DB_USER=foreman \  
DB_PASS= \  
DB_POOL=5 \  
ENCRYPTION_KEY=3694a6ccd583cd3fb7c6e60c178883b632553287 \  
ADMIN_PASS=changeme \  
ANSIBLE_ENABLED=false \  
ANSIBLE_REPO_URL=  
  
# Install dockerize  
RUN apt-get update && \  
apt-get install -y ca-certificates wget && \  
wget -q
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz &&
\  
rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
# Install Foreman  
RUN wget -q https://deb.theforeman.org/pubkey.gpg -O- | apt-key add - && \  
echo "deb http://deb.theforeman.org/ xenial $FOREMAN_RELEASE" >
/etc/apt/sources.list.d/foreman.list && \  
echo "deb http://deb.theforeman.org/ plugins $FOREMAN_RELEASE" >>
/etc/apt/sources.list.d/foreman.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
foreman=$FOREMAN_PACKAGE_VERSION \  
foreman-sqlite3 foreman-mysql2 foreman-postgresql && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
rm -f /etc/service/nginx/down /etc/nginx/sites-enabled/default  
  
# Install Ansible from source  
RUN apt-get update && apt-get install -yq python-pip && \  
git clone --depth 1 https://github.com/ansible/ansible.git /opt/ansible && \  
pip install /opt/ansible && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY files/ /  
  
CMD ["/sbin/my_init"]  

