FROM ymajik/puppetserver-standalone:stable  
LABEL maintainer="ymajik ymajik@gmail.com"  
  
ENV PUPPETDB_TERMINUS_VERSION="5.1.1" \  
PUPPETDB_URL="puppetdb" \  
PUPPETDB_PORT="8081"  
  
LABEL org.label-schema.vendor="Puppet" \  
org.label-schema.url="https://github.com/ymajik/docker-puppetserver" \  
org.label-schema.name="Puppet Server" \  
org.label-schema.license="MIT" \  
org.label-schema.version=$PUPPET_SERVER_VERSION \  
org.label-schema.vcs-url="https://github.com/ymajik/docker-puppetserver" \  
org.label-schema.vcs-ref="${VCS_REF}" \  
org.label-schema.build-date="${BUILD_DATE}" \  
org.label-schema.schema-version="1.0" \  
com.puppet.dockerfile="/Dockerfile"  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y puppetdb-
termini="$PUPPETDB_TERMINUS_VERSION"-1puppetlabs1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN puppet config set storeconfigs_backend puppetdb --section main && \  
puppet config set storeconfigs true --section main && \  
puppet config set reports puppetdb --section main  
  
COPY puppetdb.conf /etc/puppetlabs/puppet/  
  
COPY Dockerfile /  

