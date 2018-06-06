FROM python:3-slim  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
EXPOSE 5555  
# Install required packages and create a non-priveleged user  
COPY requirements.txt /  
  
ARG GOSU_VERSION=1.10  
RUN set -ex; \  
# install gosu  
\  
fetchDeps=' \  
ca-certificates \  
wget \  
'; \  
apt-get update; \  
apt-get install -y \--no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apt-get purge -y \--auto-remove $fetchDeps; \  
# add the user  
useradd -r flower; \  
# install Python dependencies  
pip install --no-cache-dir -r requirements.txt  
  
COPY docker-entrypoint.sh /  

