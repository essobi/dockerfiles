FROM ubuntu:xenial  
  
ENV \  
PUPPET_SERVER_VERSION="5.1.4" \  
PUPPET_SERVER_JAVA_ARGS="-Xms512m -Xmx512m" \  
PUPPET_DB_TERMINI_VERSION="5.1.3" \  
DNS_ALT_NAMES="puppet" \  
PATH=${PATH}:/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin  
  
RUN \  
apt-get update && \  
apt-get install -y curl lsb-release git vim make && \  
curl -s https://apt.puppetlabs.com/puppet5-release-$(lsb_release -cs).deb -o
puppet-release.deb && \  
dpkg -i puppet-release.deb && \  
rm puppet-release.deb && \  
apt-get update && \  
apt-get install -y --no-install-recommends
puppetserver=${PUPPET_SERVER_VERSION}-1$(lsb_release -cs) puppetdb-
termini=${PUPPET_DB_TERMINI_VERSION}-1$(lsb_release -cs) && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/puppetlabs/puppet/auth.conf
/etc/puppetlabs/puppet/hiera.yaml /etc/puppetlabs/pxp-agent
/etc/puppetlabs/mcollective && \  
gem install r10k && \  
puppetserver gem install hiera-eyaml deep_merge  
  
ADD conf.d/puppetserver.default /etc/default/puppetserver  
ADD conf.d/auth.* conf.d/*.conf /etc/puppetlabs/puppetserver/conf.d/  
ADD conf.d/*.xml /etc/puppetlabs/puppetserver/  
ADD bin/* /usr/local/bin/  
  
EXPOSE 8140  
ADD docker-*.sh /  
ADD docker-entrypoint.d/* /docker-entrypoint.d/  
ADD Makefile /Makefile  
  
HEALTHCHECK \--interval=10s --timeout=10s --retries=90 CMD /docker-
healthcheck.sh  
  
ENTRYPOINT [ "make" ]  
CMD [ "puppetserver" ]  

