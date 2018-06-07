FROM centos:7  
# Add EPEL  
RUN yum -y install epel-release  
  
# Java  
RUN yum -y install java-1.7.0-openjdk \  
  
# supervisord  
RUN yum -y install supervisor  
  
# Ruby  
RUN yum -y install ruby  
  
# Extra clients (ldapsearch), to help with debugging  
RUN yum -y install openldap-clients  
  
# Clean the cache  
RUN yum clean -y all  
RUN rm -rf /var/cache/yum  
  
# Install Ladle  
RUN gem install ladle  
  
RUN mkdir /data  
  
# Copy the start script for Ladle  
COPY files/run_ladle.rb /usr/bin/run_ladle.rb  
RUN chmod +x /usr/bin/run_ladle.rb  
  
# Configure default LDAP domain  
ENV LADLE_LDAP_DOMAIN 'dc=example,dc=com'  
# Copy configuration for supervisord  
COPY files/supervisord.conf /etc/supervisord.conf  
COPY files/start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Start supervisord  
CMD /start.sh  

