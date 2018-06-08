FROM ubuntu:16.04  
MAINTAINER Gareth Rushgrove "gareth@puppet.com"  
ENV PUPPET_SERVER_VERSION="2.6.0" DUMB_INIT_VERSION="1.0.2"
UBUNTU_CODENAME="xenial" PUPPETSERVER_JAVA_ARGS="-Xms256m -Xmx256m"
PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH
PUPPETDB_TERMINUS_VERSION="4.2.0"  
LABEL org.label-schema.vendor="Puppet" \  
org.label-schema.name="Puppet Server (PuppetDB backend)" \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.version=$PUPPET_SERVER_VERSION \  
com.puppet.dockerfile="/Dockerfile" \  
name="puppetserver" \  
version="1.0.0"  
  
RUN apt-get update && \  
apt-get install -y wget=1.17.1-1ubuntu1 && \  
wget https://apt.puppetlabs.com/puppetlabs-release-pc1-"$UBUNTU_CODENAME".deb
&& \  
wget https://github.com/Yelp/dumb-
init/releases/download/v"$DUMB_INIT_VERSION"/dumb-
init_"$DUMB_INIT_VERSION"_amd64.deb && \  
dpkg -i puppetlabs-release-pc1-"$UBUNTU_CODENAME".deb && \  
dpkg -i dumb-init_"$DUMB_INIT_VERSION"_amd64.deb && \  
rm puppetlabs-release-pc1-"$UBUNTU_CODENAME".deb dumb-
init_"$DUMB_INIT_VERSION"_amd64.deb && \  
apt-get update && \  
apt-get install --no-install-recommends -y
puppetserver="$PUPPET_SERVER_VERSION"-1puppetlabs1 puppetdb-
termini="$PUPPETDB_TERMINUS_VERSION"-1puppetlabs1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY puppetserver /etc/default/puppetserver  
COPY logback.xml /etc/puppetlabs/puppetserver/  
COPY request-logging.xml /etc/puppetlabs/puppetserver/  
COPY puppetdb.conf /etc/puppetlabs/puppet/  
COPY docker-entrypoint.sh /  
  
RUN chmod 0755 /docker-entrypoint.sh && \  
puppet config set autosign true \--section master && \  
puppet config set storeconfigs_backend puppetdb --section main && \  
puppet config set storeconfigs true \--section main && \  
puppet config set reports puppetdb --section main && \  
puppet config set environmentpath \$confdir/environments --section main  
  
VOLUME /etc/puppetlabs/code/  
VOLUME /etc/puppetlabs/code/  
VOLUME /etc/puppetlabs/puppet/ssl/  
VOLUME /etc/puppetlabs/puppet/environments/  
VOLUME /opt/puppetlabs/server/data/puppetserver/  
  
EXPOSE 8140  
ENTRYPOINT ["dumb-init", "/docker-entrypoint.sh"]  
CMD ["foreground" ]  
  
COPY Dockerfile /  

