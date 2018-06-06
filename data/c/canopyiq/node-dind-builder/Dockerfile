FROM node:8.11  
  
RUN set -ex; \  
\  
echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/debian-backports.list; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libxslt1-dev \  
libxml2 \  
libsm6 \  
libxext6 \  
libglib2.0-0 \  
build-essential \  
g++ \  
gcc \  
git \  
libffi-dev \  
libssl-dev \  
unzip \  
ssh \  
curl; \  
apt-get -t jessie-backports -y --no-install-recommends install git; \  
rm -rf /var/lib/apt/lists/*; \  
\  
VER="17.03.0-ce"; \  
curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz; \  
tar -xz -C /tmp -f /tmp/docker-$VER.tgz; \  
rm /tmp/docker-$VER.tgz; \  
mv /tmp/docker/* /usr/bin; \  
npm install -g lerna@2.8.0; \  
cd /opt && curl --insecure -OL
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-3.0.3.778-linux.zip && \  
unzip sonar-scanner-cli-3.0.3.778-linux.zip && rm sonar-scanner-
cli-3.0.3.778-linux.zip && \  
ln -s /opt/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner /usr/bin/

