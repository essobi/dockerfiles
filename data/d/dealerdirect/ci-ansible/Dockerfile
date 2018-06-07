FROM debian:jessie  
MAINTAINER Dealerdirect  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV BUILD_DEPS "python-pip build-essential python-dev libssl-dev libffi-dev"  
ENV INSTALL_APT "ruby sudo python python-six nodejs npm openssl curl git
parallel"  
ENV INSTALL_PIP "setuptools ansible cryptography ansible-lint yamllint flake8
pydocstyle"  
ENV INSTALL_GEM "rubocop"  
ENV INSTALL_NPM "jsonlint"  
COPY initctl_faker .  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends $INSTALL_APT \  
&& apt-get install -y --no-install-recommends $BUILD_DEPS \  
&& ln -s "$(which nodejs)" /usr/bin/node \  
&& gem install $INSTALL_GEM \  
&& pip install $INSTALL_PIP \  
&& npm install $INSTALL_NPM -g \  
&& curl -L https://github.com/AGWA/git-crypt/archive/debian/0.5.0-2.tar.gz |
tar zxv -C /var/tmp \  
&& cd /var/tmp/git-crypt-debian-0.5.0-2 \  
&& make \  
&& make install PREFIX=/usr/local \  
&& cd \- \  
&& rm -f -r /var/tmp/git-crypt-debian-0.5.0-2 \  
&& pip install --upgrade setuptools \  
&& apt-get remove -y --purge $BUILD_DEPS \  
&& apt-get -y purge \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc \  
&& rm -Rf /usr/share/man \  
&& mkdir -p /etc/ansible \  
&& echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts \  
&& chmod +x initctl_faker \  
&& rm -fr /sbin/initctl \  
&& ln -s /initctl_faker /sbin/initctl  

