FROM debian:buster-slim  
  
ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh
/usr/local/bin/  
RUN set -eux; \  
chmod +x /usr/local/bin/wait-for-it.sh; \  
apt-get update -y; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends \  
curl \  
ca-certificates \  
gnupg \  
; \  
curl -L https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add \- ;
\  
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(cut -d / -f 1
/etc/debian_version)-pgdg main" > /etc/apt/sources.list.d/pgdg.list ; \  
apt-get update -y; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends \  
build-essential \  
libc6-dev \  
libdpkg-perl \  
postgresql-client \  
postgresql-server-dev-all \  
; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

