FROM debian:stretch-slim  
MAINTAINER sysadmin@kronostechnologies.com  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV SSH_ALLOWGROUPS=root  
ENV SSSD_LDAP_DEFAULT_AUTHOK=''  
ENV SSSD_LDAP_URI=''  
ENV SSSD_LDAP_DEFAULT_BIND_DN=''  
ENV SSSD_LDAP_SEARCH_BASE=''  
ENV SSSD_LDAP_USER_SEARCH_BASE=''  
ENV SSSD_LDAP_GROUP_SEARCH_BASE=''  
ENV SSSD_LDAP_SUDO_SEARCH_BASE=''  
ENV SSL_CERTIFICATE_DOWNLOAD_URL=''  
ENV MYSQL_HOST=localhost  
ENV MYSQL_USER=root  
ENV MYSQL_PASSWORD=''  
ENV MYSQL_SSL_CA=''  
ENV MYSQL_PROMPT='docker@localhost [\\\d]>\\\\_'  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
libnss-sss \  
libpam-sss \  
libsss-sudo \  
lsb-release \  
mysql-client \  
openssh-server \  
sssd \  
sudo \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://download.docker.com/linux/debian/gpg docker.gpg  
RUN apt-key add docker.gpg \  
&& rm docker.gpg \  
&& echo "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list \  
&& apt-get update && apt-get install -y --no-install-recommends \  
docker-ce \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://github.com/kronostechnologies/docker-init-
entrypoint/releases/download/1.3.0/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
COPY ./docker/ /  
  
EXPOSE 22  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

