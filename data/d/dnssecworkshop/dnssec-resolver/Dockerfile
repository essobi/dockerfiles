# Image: dnssec-resolver  
# Startup a docker container as resolver using BIND  
FROM dnssecworkshop/dnssec-bind  
  
MAINTAINER dape16 "dockerhub@arminpech.de"  
LABEL RELEASE=20171101-2303  
  
# Set timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Install software  
RUN apt-get update  
RUN apt-get upgrade -y  
## Install tools for DNSViz  
RUN apt-get install -y --no-install-recommends make python-dnspython python-
pygraphviz  
## Install libs and tools for m2crypto patch + compile  
RUN apt-get install -y --no-install-recommends swig libssl-dev gcc python-dev
patch python-setuptools  
  
## Install further tools for web services  
RUN apt-get install -y --no-install-recommends gitweb libcgi-pm-perl  
  
## Setup apache webderver  
RUN apt-get install -y --no-install-recommends apache2  
RUN a2enmod cgi rewrite  
RUN a2dissite 000-default  
RUN mkdir /var/log/apache2/mod_cgi && chown www-data: /var/log/apache2/mod_cgi  
RUN mkdir /var/cache/git && chown www-data: /var/cache/git  
  
# Build DNSViz  
RUN cd /opt && git clone https://github.com/dnsviz/dnsviz && \  
cd dnsviz && git checkout v0.5.1 && \  
python setup.py build && python setup.py install  
  
# Compile ECDSA support into m2crypto  
RUN cd /opt && git clone https://gitlab.com/m2crypto/m2crypto.git && \  
cd m2crypto && git checkout 0.23.0 && \  
patch -p1 < /opt/dnsviz/contrib/m2crypto-0.23.patch && \  
python setup.py build && python setup.py install  
  
# Deploy DNSSEC workshop material  
RUN cd /root && git clone https://github.com/dnssec-workshop/dnssec-data && \  
rsync -v -rptgoD --copy-links /root/dnssec-data/dnssec-resolver/ /  
  
# Deploy doc wiki  
RUN cd /root && git clone https://github.com/dnssec-workshop/dnssec-doc  
  
# Activate Webserver config  
RUN a2ensite dnsviz.test gitweb.test doc.test  
  
# Configure bind nocaching resolver  
RUN mkdir -p /var/cache/bind.nocache && \  
chown bind: /var/cache/bind.nocache  
  
# Start services using supervisor  
RUN mkdir -p /var/log/supervisor  
  
EXPOSE 22 53  
CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/dnssec-
resolver.conf" ]  
  
# vim: set syntax=docker tabstop=2 expandtab:  

