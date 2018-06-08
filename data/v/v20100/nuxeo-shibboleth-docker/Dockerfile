FROM ubuntu:trusty  
MAINTAINER Vincent Lombard <vincent.lombard@universite-lyon.fr>  
  
# Set locale  
RUN locale-gen --no-purge en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV GOPATH /app  
# First install apt needed utility package  
RUN set -x \  
&& apt-get update && apt-get install -y \  
python-software-properties \  
software-properties-common wget \  
sudo \  
net-tools \  
git \  
vim \  
curl \  
zip \  
unzip \  
apache2 \  
supervisor\  
&& curl -k -O http://pkg.switch.ch/switchaai/SWITCHaai-swdistrib.asc\  
&& gpg --with-fingerprint SWITCHaai-swdistrib.asc\  
&& apt-key add SWITCHaai-swdistrib.asc\  
&& echo 'deb http://pkg.switch.ch/switchaai/ubuntu trusty main' | sudo tee
/etc/apt/sources.list.d/SWITCHaai-swdistrib.list > /dev/null\  
&& apt-get update && apt-get install -y \  
shibboleth  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#Template with mustache mo  
ADD mo /tmp/mo  
ADD apache-sp.tmpl /etc/apache2/sites-available/apache-sp.tmpl  
RUN cat /etc/apache2/sites-available/apache-sp.tmpl |/tmp/mo
>/etc/apache2/sites-available/apache-sp.conf  
ADD shibboleth2.tmpl /etc/shibboleth/shibboleth2.tmpl  
RUN cat /etc/shibboleth/shibboleth2.tmpl |/tmp/mo
>/etc/shibboleth/shibboleth2.xml  
ADD attribute-map.xml /etc/shibboleth/attribute-map.xml  
#ADD sp-cert.pem /etc/shibboleth/sp-cert.pem  
#ADD sp-key.pem /etc/shibboleth/sp-key.pem  
RUN set -x \  
&& a2enmod ssl\  
&& a2enmod proxy\  
&& a2enmod headers\  
&& a2enmod xml2enc\  
&& a2enmod proxy_http\  
&& a2dissite 000-default\  
&& a2ensite apache-sp\  
&& add-apt-repository ppa:ubuntu-lxc/lxd-stable\  
&& apt-get update && apt-get install -y \  
golang\  
&& echo "ok"\  
&& go get -u github.com/zzOzz/json-federation  
#//;go get golang.org/x/text/collate; go get golang.org/x/text/language;go
install json-federation  
#VOLUME ["/etc/shibboleth/sp-cert.pem","/etc/shibboleth/sp-key.pem"]  
ENV
FEDERATION_METADATA_SIGNING_CERT=https://metadata.federation.renater.fr/certs/renater-
metadata-signing-cert-2016.pem  
ENV
FEDERATION_METADATA_URL=https://metadata.federation.renater.fr/renater/main/main-
idps-renater-metadata.xml  
ENV SHIB_CERT_PATH=/etc/shibboleth  
RUN wget -O /etc/ssl/certs/federation-metadata-cert.pem
$FEDERATION_METADATA_SIGNING_CERT  
EXPOSE 443  
ENTRYPOINT [ "supervisord" ]  
  
#docker run -i -t shibbolethspudl_shibbolethsp /bin/bash  
#https://nuxeo.universite-
lyon.fr/Shibboleth.sso/Login?target=https%3A%2F%2Fnuxeo.universite-
lyon.fr%2Fnuxeo%2F  
#https://ish.universite-
lyon.fr/Shibboleth.sso/Login?target=https%3A%2F%2Fish.universite-
lyon.fr%2Fnuxeo%2F  
# Update/Upgrad all packages on each build  
ONBUILD RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::=--force-
confdef  

