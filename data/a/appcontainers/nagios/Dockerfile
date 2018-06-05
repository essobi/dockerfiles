############################################################  
# Dockerfile to build a Nagios/Adagios server  
# Based on appcontainers/centos66  
############################################################  
  
# Set the base image to Centos 6.6 Base  
FROM appcontainers/centos66  
  
# File Author / Maintainer  
MAINTAINER Rich Nason rnason@appcontainers.com  
  
#*************************  
#* Versions *  
#*************************  
  
  
#**********************************  
#* Override Enabled ENV Variables *  
#**********************************  
ENV APP_NAME adagios.local  
ENV APP_USER admin  
ENV APP_PASS P@ssw0rd  
  
  
#**************************  
#* Add Required Files *  
#**************************  
ADD runconfig.sh /tmp/  
ADD index.html /tmp/  
  
  
#*************************  
#* Update and Pre-Reqs *  
#*************************  
RUN rpm -ihv http://opensource.is/repo/ok-release.rpm && \  
yum clean all && \  
yum -y update && \  
rm -fr /var/cache/*  
  
  
#*************************  
#* Application Install *  
#*************************  
# Install Nagios, adagios  
RUN yum --enablerepo=ok-testing install -y pnp4nagios mk-livestatus nagios git
adagios okconfig nagios-plugins-all.x86_64 postfix  
  
# Add HTML Index file for check_http check  
RUN mv /tmp/index.html /var/www/html/  
  
# Turn on SSH for SSH Check, only listen on 127.0.0.1  
RUN sed -ie 's/#ListenAddress\ 0\\.0\\.0\\.0/ListenAddress\ 127\\.0\\.0\\.1/g'
/etc/ssh/sshd_config  
  
# Do a git commit, need to add remote host, but this will allow us to keep our
nagios configs in git  
RUN cd /etc/nagios/ && \  
git init && \  
git add . && \  
git commit -a -m "Initial commit"  
  
# Check all permissions  
RUN chown -R nagios /etc/nagios/* /etc/nagios/.git && \  
chmod -R 775 /etc/nagios  
  
# Adgios will write to /etc/nagios/adagios, ensure directory exists and
nagios.cfg knows about it.  
RUN mkdir -p /etc/nagios/adagios && \  
pynag config --append cfg_dir=/etc/nagios/adagios  
  
# Status view needs broker modules livestatus and pnp4nagios, so configure
nagios.cfg  
RUN pynag config --append "broker_module=/usr/lib64/nagios/brokers/npcdmod.o
config_file=/etc/pnp4nagios/npcd.cfg" && \  
pynag config --append "broker_module=/usr/lib64/mk-livestatus/livestatus.o
/var/spool/nagios/cmd/livestatus" && \  
pynag config --set "process_performance_data=1"  
  
# Add nagios to apache group  
RUN usermod -G apache nagios  
  
  
#************************  
#* Post Deploy Clean Up *  
#************************  
  
  
  
#**************************  
#* Config Startup Items *  
#**************************  
RUN chmod +x /tmp/runconfig.sh && \  
echo "/tmp/./runconfig.sh" >> ~/.bashrc && \  
echo "service sshd start" >> ~/.bashrc  
  
CMD /bin/bash  
  
  
#****************************  
#* Expose Applicatoin Ports *  
#****************************  
# Expose ports to other containers only  
EXPOSE 80

