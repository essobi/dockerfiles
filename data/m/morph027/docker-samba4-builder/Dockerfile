FROM ubuntu:trusty  
  
MAINTAINER morph027 "morphsen@gmx.com"  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y -qq install \  
acl \  
autoconf \  
bind9utils \  
build-essential \  
curl \  
dnsutils \  
gdb \  
git-core \  
krb5-user \  
libacl1-dev \  
libattr1-dev \  
libblkid-dev \  
libgcrypt11-dev \  
libgnutls-dev \  
libldap2-dev \  
libldb-dev \  
libpopt-dev \  
libreadline-dev \  
libtalloc-dev \  
libtevent-dev \  
pkg-config \  
python-dev \  
python-dnspython \  
resolvconf \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3 \  
&& (\curl -ksSL https://get.rvm.io | bash -s stable --ruby)  
  
ENV PATH
/usr/local/rvm/bin:/usr/local/rvm/rubies/default/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN gem install fpm --no-rdoc --no-ri  
  
RUN gem install aptly_cli --no-rdoc --no-ri  

