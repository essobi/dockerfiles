FROM python:2.7.13  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update \  
&& apt-get -y install apt-transport-https wget \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get -y update \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get -y install sendmail krb5-config krb5-user python-ldap libsasl2-dev
python-dev libldap2-dev libssl-dev xmlsec1 libfontconfig nodejs yarn vagrant
openssh-client jq bsdmainutils unzip vim \  
&& apt-get -y install postgresql \  
&& apt-get -y install --upgrade python3 \  
&& npm install -g grunt-cli \  
&& sed -i 's/peer$/trust/g; s/md5$/trust/g' $(find /etc/postgresql -name
pg_hba.conf) \  
&& service postgresql restart \  
&& curl -fsSL get.docker.com | sh \  
&& curl -L https://github.com/docker/compose/releases/download/1.20.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& wget 'https://storage.googleapis.com/shellcheck/shellcheck-
latest.linux.x86_64.tar.xz' \  
&& xz -d ./shellcheck-latest.linux.x86_64.tar.xz \  
&& tar -xvf ./shellcheck-latest.linux.x86_64.tar \  
&& cp ./shellcheck-latest/shellcheck /usr/bin/ \  
&& chmod 755 /usr/bin/shellcheck \  
&& rm -rf /var/lib/apt/lists/*  

