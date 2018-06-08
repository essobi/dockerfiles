# Create a storage container before running this:  
#  
# docker run --name razor-repo -v /var/lib/razor/repo-store -v /var/lib/pgsql
-v /var/logs tianon/true  
#  
# Start centos-razor-server and attach storage and link ports.  
#  
# docker run --name razor-server --hostname razor-server -d --volumes-from
razor-repo \  
# -p 8080:8080 sedlund/centos-razor-server  
#  
# The first time this is run the /start.sh script will set up the db if it has  
# not been yet. It will also check for the razor microkernel and grab and
unpack it.  
#  
# You will then need a DHCP and TFTP server to point to this container, and a  
# razor-client installed somewhere to interact with this container.  
#  
FROM tianon/centos:6.5  
RUN yum -y update  
  
RUN rpm -ivh https://yum.puppetlabs.com/el/6/products/x86_64/puppetlabs-
release-6-10.noarch.rpm && \  
yum install -y puppet tar  
  
ADD razor-postgres-install.pp /  
ADD start.sh /  
  
ENV HOSTNAME razor-server  
ENV TORQUEBOX_HOME /opt/razor-torquebox  
ENV JBOSS_HOME $TORQUEBOX_HOME/jboss  
ENV JRUBY_HOME $TORQUEBOX_HOME/jruby  
ENV PATH $JRUBY_HOME/bin:$PATH  
  
RUN puppet module install puppetlabs/postgresql  
RUN puppet module install puppetlabs/razor  
RUN puppet apply -e 'include razor'  
  
# 69 TFTP  
# 8080 Torquebox API  
EXPOSE 8080  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  

