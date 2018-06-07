FROM chtijbug/drools-platform-docker  
MAINTAINER Nicolas Héron  
  
# to copy Puppet code into container  
ADD drools_platform_puppet_withexamples /drools_platform_puppet_withexamples  
#to run Puppet code  
RUN puppet apply -d drools_platform_puppet_withexamples/manifests/site.pp
--confdir=drools_platform_puppet_withexamples/
--modulepath=/etc/puppet/modules:drools_platform_puppet_withexamples/modules:
--libdir=drools_platform_puppet_withexamples/modules/lib --verbose  
  
USER root  
  
# clean packages  
RUN apt-get clean  
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# tomcat7  
EXPOSE 8080  
# Expose the PostgreSQL and SSH port  
EXPOSE 22  
EXPOSE 5432  
EXPOSE 61616  
##RUN /bin/sh /tmp/set-psql-password.sh  
CMD ["/usr/bin/supervisord"]  
  

