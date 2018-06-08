FROM ubuntu:14.04  
  
ENV PUPPET_COLLECTION pc1  
  
# Install puppetlabs apt archive  
RUN \  
apt update \  
&& apt install -y wget \  
&& wget \  
"https://apt.puppetlabs.com/puppetlabs-
release-${PUPPET_COLLECTION}-trusty.deb" \  
-O /tmp/puppetlabs-release.deb \  
&& dpkg -i /tmp/puppetlabs-release.deb \  
&& rm -f /tmp/puppetlabs-release.deb \  
&& apt remove --purge -y wget \  
&& apt-get clean \  
&& find /var/cache/apt /var/lib/apt/lists -type f -delete  
  
# Install puppetserver,  
# set up logging  
RUN \  
apt update \  
&& apt install -y puppetserver puppetdb-termini \  
&& rm -rf /var/log/puppetlabs/puppetserver/* \  
&& ln -s /dev/stdout /var/log/puppetlabs/masterhttp.log \  
&& ln -s /dev/stdout /var/log/puppetlabs/puppetserver-access.log \  
&& ln -s /dev/stdout /var/log/puppetlabs/puppetserver.log \  
&& ln -s /opt/puppetlabs/puppet/bin/puppet \  
/opt/puppetlabs/server/bin/puppetserver \  
/usr/local/sbin/ \  
&& apt-get clean \  
&& find /var/cache/apt /var/lib/apt/lists -type f -delete  
  
copy run-puppet.sh /usr/local/sbin/  
copy puppet.conf.tmpl puppet.conf.puppetdb.tmpl puppetdb.conf.tmpl \  
routes.yaml.tmpl /etc/puppetlabs/puppet/  
  
EXPOSE 8140  
  
VOLUME /etc/puppetlabs/puppet/ssl /etc/puppetlabs/code  
  
CMD ["run-puppet.sh"]  
  

