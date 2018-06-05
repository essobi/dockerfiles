FROM debian:9  
MAINTAINER Gareth Rushgrove "gareth@puppet.com"  
ENV PUPPETDB_VERSION="5.1.3" PUPPET_AGENT_VERSION="5.3.3"
DUMB_INIT_VERSION="1.2.1" DEBIAN_CODENAME="stretch" PUPPETDB_USER=puppetdb
PUPPETDB_PASSWORD=puppetdb PUPPETDB_JAVA_ARGS="-Djava.net.preferIPv4Stack=true
-Xms256m -Xmx256m"
PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH  
  
LABEL org.label-schema.vendor="Puppet" \  
org.label-schema.url="https://github.com/puppetlabs/puppet-in-docker" \  
org.label-schema.name="PuppetDB" \  
org.label-schema.license="Apache-2.0" \  
org.label-schema.version=$PUPPETDB_VERSION \  
org.label-schema.vcs-url="https://github.com/puppetlabs/puppet-in-docker" \  
org.label-schema.vcs-ref="a2b1fbbc73177ddc3def23d167f9beb9c3ef9f6c" \  
org.label-schema.build-date="2017-02-21T17:25:14Z" \  
org.label-schema.schema-version="1.0" \  
com.puppet.dockerfile="/Dockerfile"  
  
RUN apt-get update && \  
apt-get install -y wget netcat lsb-release cron && \  
wget https://apt.puppetlabs.com/puppet5-release-"$DEBIAN_CODENAME".deb && \  
wget https://github.com/Yelp/dumb-
init/releases/download/v"$DUMB_INIT_VERSION"/dumb-
init_"$DUMB_INIT_VERSION"_amd64.deb && \  
dpkg -i puppet5-release-"$DEBIAN_CODENAME".deb && \  
dpkg -i dumb-init_"$DUMB_INIT_VERSION"_amd64.deb && \  
echo "deb http://ftp.fr.debian.org/debian/ ${DEBIAN_CODENAME}-backports main
contrib non-free" > /etc/apt/sources.list.d/debian_backports.list && \  
rm puppet5-release-"$DEBIAN_CODENAME".deb dumb-
init_"$DUMB_INIT_VERSION"_amd64.deb && \  
apt-get update && \  
apt-get install --no-install-recommends -y ca-certificates-java openjdk-8-jre-
headless && \  
apt-get install --no-install-recommends -y puppet-
agent="$PUPPET_AGENT_VERSION"-1"$DEBIAN_CODENAME"
puppetdb="$PUPPETDB_VERSION"-1"$DEBIAN_CODENAME" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY puppetdb /etc/default/  
COPY logging /etc/puppetlabs/puppetdb/logging  
  
RUN rm -fr /etc/puppetlabs/puppetdb/conf.d  
COPY conf.d /etc/puppetlabs/puppetdb/conf.d  
  
# Persist the agent SSL certificate.  
VOLUME /etc/puppetlabs/puppet/ssl/  
# /etc/puppetlabs/puppetdb/ssl is automatically populated from here and  
# doesn't need a separate volume.  
COPY docker-entrypoint.sh /  
  
EXPOSE 8080 8081  
ENTRYPOINT ["dumb-init", "/docker-entrypoint.sh"]  
CMD ["foreground"]  
  
COPY Dockerfile /  

