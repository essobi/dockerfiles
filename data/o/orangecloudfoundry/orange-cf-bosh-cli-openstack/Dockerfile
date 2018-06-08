FROM orangecloudfoundry/orange-cf-bosh-cli:latest  
MAINTAINER Christophe LE COZ [OCB]  
  
USER root  
  
# Add default packages  
RUN apt-get update && \  
apt-get install -y maven gradle openjdk-8-jdk npm python-dev python-pip jq &&
\  
apt-get clean && \  
apt-get autoremove -y && \  
apt-get purge  
  
# Openstack CLI  
RUN export LC_ALL=C && \  
pip install --upgrade pip && \  
pip install python-openstackclient  
  
# Final settings & Cleanup  
RUN echo "Java `java -version 2>&1 | grep version`" >> /etc/motd && \  
echo "`mvn -version 2>&1 | grep "Apache Maven"`" >> /etc/motd && \  
echo "`python --version 2>&1`" >> /etc/motd && \  
echo "pip `pip --version 2>&1 | awk '{print $2}'` - Python package manager" >>
/etc/motd && \  
echo "npm `npm --version` - npm is the package manager for JavaScript" >>
/etc/motd && \  
echo "" >> /etc/motd && \  
echo "Openstack cli `openstack --version 2>&1 | awk '{print $2}'` -
OpenStackClient project provides a unified command-line client" >> /etc/motd
&& \  
echo "The following individual clients are deprecated in favor of a common
client." >> /etc/motd && \  
echo " * Nova `nova --version 2>&1` - Compute API and extensions" >> /etc/motd
&& \  
echo " * Glance `glance --version 2>&1` - Image service API" >> /etc/motd && \  
echo " * Cinder `cinder --version 2>&1` - Block Storage API and extensions" >>
/etc/motd && \  
echo "" >> /etc/motd && \  
find /var/log -type f -delete && \  
rm -Rf /tmp/* && \  
touch /var/log/lastlog && \  
chgrp utmp /var/log/lastlog && \  
chmod 664 /var/log/lastlog  
  
# Launch supervisord daemon  
EXPOSE 22  
CMD /usr/local/bin/supervisord  

