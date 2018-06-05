FROM debian:jessie  
  
EXPOSE 8080 8081  
ENV RELEASE=jessie \  
  
LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
  
PUPPETDB_VERSION=4.4.0-1puppetlabs1 \  
  
POSTGRES_SUBNAME=//postgresql:5432/puppetdb \  
POSTGRES_USER=puppetdb \  
POSTGRES_PASSWORD=puppetdb \  
  
PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH  
  
RUN apt-get update \  
&& apt-get install -y curl locales-all \  
&& curl -O http://apt.puppetlabs.com/puppetlabs-release-pc1-${RELEASE}.deb \  
&& dpkg -i puppetlabs-release-pc1-${RELEASE}.deb \  
&& rm puppetlabs-release-pc1-${RELEASE}.deb \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y puppetdb=$PUPPETDB_VERSION puppet-agent \  
&& rm -rf /var/lib/apt/lists/*  
  
# Setting  
RUN puppet config set dns_alt_names puppetdb --section agent  
  
# things done by "puppetdb ssl-setup -f" at first run  
RUN printf 'set /augeas/context /files//jetty.ini/jetty \n\  
set ssl-host "0.0.0.0" \n\  
set ssl-port "8081" \n\  
set ssl-key "/etc/puppetlabs/puppetdb/ssl/private.pem" \n\  
set ssl-cert "/etc/puppetlabs/puppetdb/ssl/public.pem" \n\  
set ssl-ca-cert "/etc/puppetlabs/puppetdb/ssl/ca.pem" \n\  
print . \n\  
' | /opt/puppetlabs/puppet/bin/augtool -Ast "Puppet.lns incl
/etc/puppetlabs/puppetdb/conf.d/jetty.ini"  
  
# Allow JAVA_ARGS tuning  
RUN sed -i -e 's@^JAVA_ARGS=\\(.*\\)$@JAVA_ARGS=\$\\{JAVA_ARGS:-\1\\}@'
/etc/default/puppetdb  
  
# Configure entrypoint  
COPY docker-entrypoint.sh /  
COPY docker-entrypoint.d/* /docker-entrypoint.d/  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["puppetdb", "foreground"]  

