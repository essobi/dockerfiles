FROM ubuntu:trusty  
  
MAINTAINER ramzthecoder@gmail.com  
  
EXPOSE 8080 8140  
ENV \  
PUPPET_AGENT_VERSION=1.5.2-1trusty \  
PUPPETSERVER_VERSION=2.4.0-1puppetlabs1 \  
PUPPETDB_VERSION=4.1.0-1puppetlabs1 \  
PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& curl -O http://apt.puppetlabs.com/puppetlabs-release-pc1-trusty.deb \  
&& dpkg -i puppetlabs-release-pc1-trusty.deb \  
&& apt-get update \  
&& apt-get install -y --force-yes git \  
puppet-agent=$PUPPET_AGENT_VERSION \  
puppetserver=$PUPPETSERVER_VERSION \  
puppetdb-termini=$PUPPETDB_VERSION \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /etc/puppetlabs-template && cp -Rf /etc/puppetlabs/*
/etc/puppetlabs-template/.  
VOLUME ["/etc/puppetlabs"]  
  
# Configure entrypoint  
COPY /docker-entrypoint.sh /usr/local/bin/  
COPY /docker-entrypoint.d/* /usr/local/bin/docker-entrypoint.d/  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["puppetserver", "foreground"]  

