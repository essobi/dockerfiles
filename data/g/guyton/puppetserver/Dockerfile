FROM guyton/centos7  
ENV PUPPET_SERVER_VERSION="2.7.2"  
RUN rpm -Uvh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm  
RUN useradd -u 140 puppet  
RUN yum install -y puppetserver-$PUPPET_SERVER_VERSION; yum clean all  
CMD /opt/puppetlabs/bin/puppetserver foreground  
EXPOSE 8140  
VOLUME /etc/puppetlabs /opt/puppetlabs/server/data/puppetserver
/var/log/puppetlabs/puppetserver  
  
#  
# Fix up JAVA_ARGS to remove obsolete param and allow for override by setting
JAVA_ARGS as docker env variable  
#  
RUN mv /etc/sysconfig/puppetserver /etc/sysconfig/puppetserver-orig; cat
/etc/sysconfig/puppetserver-orig | sed -e 's/-Xms2g -Xmx2g
-XX:MaxPermSize=256m/\${JAVA_ARGS:--Xms2g -Xmx2g}/' >
/etc/sysconfig/puppetserver  
  
#  
# Create a set of staging archives of /etc/puppetlabs and
/opt/puppetlabs/server/data/puppetserver  
#  
# With this, can run alternate CMD "initialize" to place these files in a new
instance's externally mounted volumes when first setting up.  
# "initialize" will run "tar zx --skip-old-files -f
/tmp/etc_puppetlabs_init.tar.gz" and similar for the puppetserver data archive  
#  
RUN tar zcf /tmp/etc_puppetlabs_init.tar.gz /etc/puppetlabs ; tar zcf
/tmp/opt_puppetlabs_server_data_puppetserver.tar.gz
/opt/puppetlabs/server/data/puppetserver  
COPY initialize /usr/local/bin/initialize  
  
#  
# Ideas for extending/customizing your own image:  
#  
# RUN /opt/puppetlabs/puppet/bin/puppet config set autosign true --section
master;  
# RUN /opt/puppetlabs/puppet/bin/puppet config set certname 'my-puppetserver-
hostname.example.net' --section master  

