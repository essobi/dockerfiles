# Use CentOS 7 base image from Docker Hub  
FROM centos:centos7  
MAINTAINER Jose De la Rosa "https://github.com/jose-delarosa"  
# Do overall update and install missing packages needed for OpenManage  
RUN yum -y update  
RUN yum -y install gcc wget perl passwd which tar net-snmp  
RUN yum -y install libstdc++.so.6 compat-libstdc++-33.i686 glibc.i686  
  
# Set login credentials  
RUN echo 'root:password' | chpasswd  
  
# Define OMSA repo  
RUN wget -q -O - http://linux.dell.com/repo/hardware/dsu/bootstrap.cgi | bash  
  
# Install all but we could select specific components to reduce image size  
RUN yum -y install srvadmin-all  
  
# Fix storage recognition  
RUN sed -i -e 's/\x00release_date\x00/\x00version\x00\x00\x00\x00\x00\x00/'
/opt/dell/srvadmin/lib64/libstorelib.so.4.39-0  
  
# Add to PATH  
ENV PATH $PATH:/opt/dell/srvadmin/bin:/opt/dell/srvadmin/sbin  
  
# Fix insecure default webserver settings  
#RUN omconfig preferences webserver attribute=sslencryption
setting=autonegotiate  
#RUN omconfig preferences webserver attribute=signalgorithm setting=SHA256  
#RUN omconfig preferences webserver attribute=gennewcert cn=hostname org=OMSA
OU=IT location=Docker state=none country=DE keysize=2048 webserverrestart=true  
# Clean cache to minimize container image  
RUN yum clean all  
  
# Restart application to ensure a clean start  
CMD srvadmin-services.sh restart && snmpd && tail -f
/opt/dell/srvadmin/var/log/openmanage/dcsys64.xml  

