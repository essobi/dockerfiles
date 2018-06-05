######################################################  
#  
# Agave DevOps GridEngine Server  
# Tag: agaveapi/gridengine  
#  
# This container provides a standard pbs controller  
# and worker created on top of the agaveapi/centos-base  
# image. Nothing special here.  
#  
# Usage:  
# docker run -h docker.example.com -i -t \  
# -p 10022:22 \ # SSHD, SFTP  
# --rm agaveapi/gridengine  
#  
# https://bitbucket.org/taccaci/agave-environment  
#  
######################################################  
  
FROM agaveapi/centos-base  
  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>  
  
# Install GridEngine  
RUN yum -y install gridengine gridengine-qmaster gridengine-execd gridengine-
qmon gridengine-devel vim-minimal  
  
# Configure GridEngine  
WORKDIR /usr/share/gridengine/  
  
ADD gridengine/docker_configuration.conf
/usr/share/gridengine/docker_configuration.conf  
ADD gridengine/hostgroup.conf /usr/share/gridengine/hostgroup.conf  
ADD gridengine/debug.queue /usr/share/gridengine/debug.queue  
  
# Add an entry for the docker host which will be available in the runtime
container,  
# but which is missing during builds  
RUN echo "$(grep "$HOSTNAME" /etc/hosts | awk '{print $1;}') docker" >>
/etc/hosts && \  
cat /etc/hosts  
  
## Patch the os check which does not suppor thtis version of linux  
RUN sed -i 's/osrelease="`$UNAME -r`"/osrelease="2.6.1"/g' util/arch  
  
# Install the master and execution servers  
RUN echo "$(grep "$HOSTNAME" /etc/hosts | awk '{print $1;}') docker" >>
/etc/hosts && \  
echo "domain docker" >> /etc/resolv.conf && \  
./inst_sge -x -m -auto /usr/share/gridengine/docker_configuration.conf && \  
cd /usr/share/gridengine/default/common && \  
source /usr/share/gridengine/default/common/settings.sh && \  
echo docker > act_qmaster && \  
qconf -Mhgrp /usr/share/gridengine/hostgroup.conf && \  
qconf -Aq /usr/share/gridengine/debug.queue && \  
qconf -Mq /usr/share/gridengine/debug.queue  
  
# Add in a test submit script  
ADD gridengine/gridengine.submit /home/testuser/gridengine.submit  
RUN chown testuser:testuser /home/testuser/gridengine.submit  
  
ADD supervisord.conf /etc/supervisord.conf  
RUN mkdir /var/log/supervisor  
RUN chmod -R 777 /var/log/supervisor  
RUN unset HOSTNAME  
  
# Add entrypoint script to set the current hostname so the scheduler can
communicat  
ADD docker_entrypoint.sh /docker_entrypoint.sh  
  
ENTRYPOINT [ "/docker_entrypoint.sh" ]  
EXPOSE 10389 22  
CMD ["/usr/bin/supervisord"]  

