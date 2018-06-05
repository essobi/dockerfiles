## Dockerfile for gitolite with HTTP support  
FROM debian:wheezy  
MAINTAINER Hyzual "hyzual@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# make the "en_US.UTF-8" locale  
RUN apt-get update -q \  
&& apt-get install -y locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
ENV APACHE_VERSION 2.2.22-13+deb7u4  
ENV GITOLITE_VERSION 3.6.2  
ENV GITOLITE_URL
https://github.com/sitaramc/gitolite/archive/v$GITOLITE_VERSION.tar.gz  
  
# download and install apache, suexec and gitolite  
RUN apt-get update -q \  
&& apt-get install -y --no-install-recommends \  
apache2=$APACHE_VERSION \  
apache2-suexec-custom \  
apache2-utils \  
ca-certificates \  
git \  
openssh-server \  
wget \  
&& wget --quiet --output-document /tmp/gitolite-source.tar.gz $GITOLITE_URL \  
&& tar -xzf /tmp/gitolite-source.tar.gz -C /tmp/ \  
&& /tmp/gitolite-$GITOLITE_VERSION/install -to /usr/local/bin \  
&& rm -rf /tmp/gitolite-source /tmp/gitolite-source.tar.gz \  
&& apt-get purge -y --auto-remove wget \  
&& rm -r /var/lib/apt/lists/*  
  
RUN adduser --disabled-login --gecos 'Gitolite' \--home /data --no-create-home
git \  
&& mkdir -p /var/run/sshd \  
&& install -d -m 0755 -o git -g git /var/www/bin \  
&& install -d -m 0755 /var/www/git \  
&& a2enmod suexec  
  
# Calls gitolite-shell. We need it to avoid installing gitolite in apache's
document root.  
COPY ./gitolite-suexec-wrapper.sh /var/www/bin/gitolite-suexec-wrapper.sh  
# Apache conf for gitolite with http. It is enabled in start.sh  
COPY ./gitolite.conf /etc/apache2/sites-available/gitolite  
# Startup script  
COPY ./start.sh /start.sh  
  
RUN chmod 0700 /var/www/bin/gitolite-suexec-wrapper.sh \  
&& chown git:git /var/www/bin/gitolite-suexec-wrapper.sh  
  
VOLUME ["/data", "/repositories"]  
  
EXPOSE 22 80  
CMD ["/start.sh"]  

