FROM ubuntu:16.04  
LABEL maintainer="ymajik ymajik@gmail.com"  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
ENV PUPPET_SERVER_VERSION="5.3.0" \  
DUMB_INIT_VERSION="1.2.1" \  
UBUNTU_CODENAME="xenial" \  
PUPPETSERVER_JAVA_ARGS="-Xms256m -Xmx256m" \  
PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH
\  
PUPPET_HEALTHCHECK_ENVIRONMENT="production" \  
TZ="Europe/Brussels"  
LABEL org.label-schema.vendor="Puppet" \  
org.label-schema.url="https://github.com/ymajik/docker-puppetserver-
standalone" \  
org.label-schema.name="Puppet Server (No PuppetDB)" \  
org.label-schema.license="MIT" \  
org.label-schema.version=$PUPPET_SERVER_VERSION \  
org.label-schema.vcs-url="https://github.com/ymajik/docker-puppetserver-
standalone" \  
org.label-schema.vcs-ref="${VCS_REF}" \  
org.label-schema.build-date="${BUILD_DATE}" \  
org.label-schema.schema-version="1.0" \  
com.puppet.dockerfile="/Dockerfile"  
  
RUN apt-get update && \  
apt-get install -y wget=1.17.1-1ubuntu1 tzdata && \  
wget https://apt.puppetlabs.com/puppet5-release-"$UBUNTU_CODENAME".deb && \  
wget https://github.com/Yelp/dumb-
init/releases/download/v"$DUMB_INIT_VERSION"/dumb-
init_"$DUMB_INIT_VERSION"_amd64.deb && \  
dpkg -i puppet5-release-"$UBUNTU_CODENAME".deb && \  
dpkg -i dumb-init_"$DUMB_INIT_VERSION"_amd64.deb && \  
rm puppet5-release-"$UBUNTU_CODENAME".deb dumb-
init_"$DUMB_INIT_VERSION"_amd64.deb && \  
apt-get update && \  
apt-get install --no-install-recommends -y
puppetserver="$PUPPET_SERVER_VERSION"-1"$UBUNTU_CODENAME" && \  
gem install --no-rdoc --no-ri r10k && \  
rm /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
echo "${TZ}" > /etc/timezone && \  
ln -snf /usr/share/zoneinfo/"${TZ}" /etc/localtime && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY puppetserver /etc/default/puppetserver  
COPY logback.xml /etc/puppetlabs/puppetserver/  
COPY request-logging.xml /etc/puppetlabs/puppetserver/  
  
RUN puppet config set autosign true \--section master  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 8140  
ENTRYPOINT ["dumb-init", "/docker-entrypoint.sh"]  
CMD ["foreground" ]  
  
HEALTHCHECK \--interval=1800s --timeout=10s --retries=90 CMD \  
curl --fail -H 'Accept: pson' \  
\--resolve 'puppet:8140:127.0.0.1' \  
\--cert $(puppet config print hostcert) \  
\--key $(puppet config print hostprivkey) \  
\--cacert $(puppet config print localcacert) \  
https://puppet:8140/${PUPPET_HEALTHCHECK_ENVIRONMENT}/status/test \  
| grep -q '"is_alive":true' \  
|| exit 1  
  
COPY Dockerfile /  

