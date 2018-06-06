FROM easycom/base:jessie  
MAINTAINER Frédéric T <xmedias@easycom.digital>  
  
# =========================================  
# Update apt-cache and install requirements for common projetcs using sass and
gulp throw nodejs  
# =========================================  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && apt-get install -y wget \  
&& wget https://www.dotdeb.org/dotdeb.gpg \  
&& apt-key add dotdeb.gpg \  
&& rm dotdeb.gpg \  
&& echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list \  
&& echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.list \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install unzip \  
zip \  
wget \  
less \  
git \  
lsb-release \  
gzip \  
bzip2 \  
openssh-server \  
rsync \  
ca-certificates \  
curl \  
imagemagick \  
graphicsmagick \  
mysql-client \  
php7.0-bz2 \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-gd \  
php7.0-imagick \  
php7.0-intl \  
php7.0-json \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-mysql \  
php7.0-opcache \  
php7.0-redis \  
php7.0-soap \  
php7.0-xml \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-zip \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get -y --no-install-recommends install nodejs  
  
# =========================================  
# Install custom motd  
# =========================================  
# Copy, change rights "run.sh"  
ADD ./motd.sh /etc/profile.d/easycom_motd.sh  
RUN chmod 755 /etc/profile.d/easycom_motd.sh  
  
# =========================================  
# Install update-notifier-common  
# =========================================  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
\  
python-apt \  
gettext-base \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& wget http://ftp.de.debian.org/debian/pool/main/u/update-notifier/update-
notifier-common_0.99.3debian11_all.deb \  
&& dpkg -i update-notifier-common_0.99.3debian11_all.deb \  
&& rm update-notifier-common_0.99.3debian11_all.deb  
  
# =========================================  
# Configure SSHD  
# =========================================  
RUN sed -ri 's,^PermitRootLogin\s+.*,PermitRootLogin no,' /etc/ssh/sshd_config
\  
&& sed -ri 's,UsePAM yes,#UsePAM yes,g' /etc/ssh/sshd_config \  
&& sed -ri 's,#PasswordAuthentication yes,PasswordAuthentication no,g'
/etc/ssh/sshd_config \  
&& sed -ri 's,^X11Forwarding\s+.*,X11Forwarding no,' /etc/ssh/sshd_config \  
&& sed -ri 's,^HostKey /etc/ssh/ssh_host_,HostKey /etc/ssh/keys/ssh_host_,'
/etc/ssh/sshd_config \  
&& mkdir /etc/ssh/keys \  
&& chmod go-rwx /etc/ssh/keys \  
&& mv /etc/ssh/ssh_host_* /etc/ssh/keys/ \  
&& mkdir /var/run/sshd \  
&& service ssh stop  
  
# =========================================  
# Create user  
# =========================================  
RUN date +%s | base64 | head -c 32 > ./.pass \  
&& useradd -ms /bin/bash --password='$(cat ./.pass)' easycom \  
&& adduser easycom ssh \  
&& echo "$(cat ./.pass)\n$(cat ./.pass)\n" | passwd easycom \  
&& mv ./.pass /home/easycom/ \  
&& chown -Rf easycom:easycom /home/easycom  
  
ADD ./bashrc.easycom /home/easycom/.bashrc  
  
# =========================================  
# Our capistrano script will create a local git after deploy to allow remote
check of unallowed local changes ; so git must be configured  
# =========================================  
USER easycom  
RUN git config --global user.email "easycom-$(cat
/etc/hostname)@easycom.digital" \  
&& git config --global user.name "User Easycom - Docker Capistrano $(cat
/etc/hostname)"  
USER root  
  
ADD docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 22  
# Launch run script  
CMD ["-D"]  

