FROM bcit/centos:7  
ENV HOME=/opt/puppetlabs/server/data/puppetserver  
ENV
PATH=/opt/puppetlabs/server/bin:/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH  
ENV RUNUSER=puppet  
ENV PUPPET_HEALTHCHECK_ENVIRONMENT=production  
ENV PUPPET_CERTNAME=puppetserver  
ENV PUPPET_CERT_ALTNAMES="puppetserver.puppet.svc,puppetserver,puppet"  
ENV PUPPET_SERVERNAME=puppetserver  
  
RUN yum -y install https://yum.puppet.com/puppet/puppet5-release-
el-7.noarch.rpm \  
&& rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-puppet5 \  
&& yum -y install \  
puppetdb-termini \  
puppetserver \  
&& rm -rf /var/cache/yum  
  
COPY puppetdb.conf /etc/puppetlabs/puppet/puppetdb.conf  
  
COPY 10-resolve-userid.sh /docker-entrypoint.d/10-resolve-userid.sh  
COPY 60-puppet-conf.sh /docker-entrypoint.d/60-puppet-conf.sh  
  
RUN chmod 775 /opt/puppetlabs \  
&& chown -R 0:0 /opt/puppetlabs \  
&& find /opt/puppetlabs -type d | xargs chmod g+rwx \  
&& find /opt/puppetlabs -type f | xargs chmod g+rw  
  
RUN chmod 775 /etc/puppetlabs \  
&& find /etc/puppetlabs -type d \  
| xargs -I % \  
sh -c 'chown 0:0 %; chmod g+rwx %'  
  
# Logging config  
RUN rm -rf /var/log/puppetlabs \  
&& chmod 775 /var/log  
COPY 50-varlog.sh /docker-entrypoint.d/50-varlog.sh  
COPY logback.xml /etc/puppetlabs/puppetserver/logback.xml  
COPY request-logging.xml /etc/puppetlabs/puppetserver/request-logging.xml  
  
RUN chown 0:0 /etc/puppetlabs/code \  
&& chmod 775 /etc/puppetlabs/code  
VOLUME /etc/puppetlabs/code  
COPY 50-production.sh /docker-entrypoint.d/50-production.sh  
  
COPY puppetserver /etc/default/puppetserver  
COPY foreground /opt/puppetlabs/server/apps/puppetserver/cli/apps/foreground  
  
RUN chmod 775 /opt/puppetlabs/server/apps/puppetserver/cli/apps/foreground \  
&& chmod 775 /etc  
  
RUN tar czf /opt/puppetlabs/server.tar.gz -C /opt/puppetlabs server  
RUN rm -rf /opt/puppetlabs/server \  
&& chown 0:0 /opt/puppetlabs \  
&& chmod 775 /opt/puppetlabs  
  
ADD 50-puppetserver-server.sh /docker-entrypoint.d/50-puppetserver-server.sh  
  
COPY puppet.conf /etc/puppetlabs/puppet/puppet.conf  
RUN chmod g+rw /etc/puppetlabs/puppet/puppet.conf  
  
HEALTHCHECK \--interval=10s --timeout=10s --retries=90 CMD \  
curl --fail -H 'Accept: pson' \  
\--resolve 'puppet:8140:127.0.0.1' \  
\--cert $(puppet config print hostcert) \  
\--key $(puppet config print hostprivkey) \  
\--cacert $(puppet config print localcacert) \  
https://puppet:8140/${PUPPET_HEALTHCHECK_ENVIRONMENT}/status/test \  
| grep -q '"is_alive":true' \  
|| exit 1  
  
EXPOSE 8140  
CMD [ "/opt/puppetlabs/bin/puppetserver", "foreground" ]  

