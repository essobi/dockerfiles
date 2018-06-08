# For ubuntu, the latest tag points to the LTS version, since that is  
# recommended for general use.  
FROM ubuntu:latest  
  
RUN : \  
## For local build in China, uncomment the below lines to use aliyun mirror  
# && printf '\  
# deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe
multiverse\n\  
# deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
universe multiverse\n\  
# deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
universe multiverse\n\  
# deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted
universe multiverse\n\  
# deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted
universe multiverse\n\  
# ' > /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
samba \  
ca-certificates \  
gpg \  
dirmngr \  
wget \  
&& rm -fr /var/lib/apt/lists/*  
  
# grab gosu for easy step-down from root  
RUN set -x \  
&& GOSU_VERSION=1.10 \  
&& GPG_KEYS=B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
# && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& ( gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
|| gpg --keyserver pgp.mit.edu --recv-keys "$GPG_KEYS" \  
|| gpg --keyserver keyserver.pgp.com --recv-keys "$GPG_KEYS" ) \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget dirmngr gpg  
  
ENV SMB_CONF_DIR /var/samba  
RUN mkdir -p "$SMB_CONF_DIR"  
  
COPY docker-entrypoint.sh /usr/local/bin  
COPY usradmin smb_export smb_import /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 139 445  
CMD ["smb", "start"]  

