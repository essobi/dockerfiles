## Container containing a Torque scheduling server inside ubuntu  
### and access via ssh to a 'app' user.  
### To use as a service, SSH to this container as user app.  
### It is suggested to put job scripts in /scratch (that you might  
### want to create as a data volume for efficiency  
###  
### Note! Torque-mom requires that 'ulimit -l unlimited' is set. To achieve  
### This, you need to run this container with the '--privileged' option  
# Based on original image from AiiDA Team <info@aiida.net>  
# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
# Note also that we use phusion because, as explained on the  
# http://phusion.github.io/baseimage-docker/ page, it automatically  
# contains and starts all needed services (like logging), it  
# takes care of sending around signals when stopped, etc.  
FROM phusion/baseimage:0.9.22  
MAINTAINER João Antonio Ferreira <joao.parana@>  
  
# Install required packages  
RUN apt-get update \  
&& apt-get install -y \  
torque-scheduler \  
torque-server \  
torque-mom \  
torque-client \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean all  
  
# Enable SSH  
RUN rm -f /etc/service/sshd/down && \  
echo "UsePAM yes" >> /etc/ssh/sshd_config  
  
## Note: I don't do this in ann image. Rather,  
## I let it do it at runtime for security.  
##  
## Regenerate SSH host keys. baseimage-docker does not contain any, so you  
## have to do that yourself. You may also comment out this instruction; the  
## init system will auto-generate one during boot.  
#RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
# Put needed scripts (these will be run before the services)  
RUN mkdir -p /etc/my_init.d  
COPY ./scripts/setup-hostnames.sh /etc/my_init.d/01_setup-hostnames.sh  
  
# This must coincide with the value set in setup-hostnames.sh  
ENV HOSTNAME torquessh  
  
# Set the hostname by hand in the various configuration files  
RUN echo "$HOSTNAME" > /etc/torque/server_name && \  
echo '$pbsserver '"$HOSTNAME" > /var/spool/torque/mom_priv/config && \  
echo "$HOSTNAME np=1" > /var/spool/torque/server_priv/nodes  
  
# Start the service to allow reconfiguration and configure it. On the same
line  
# to avoid caching and to have the service up in the container, otherwise it  
# shuts down. It is also needed to run the setup-hostnames.sh script to  
# rewrite/reset the /etc/hosts (this is needed by torque)  
RUN /etc/my_init.d/01_setup-hostnames.sh && \  
/etc/init.d/torque-server start && \  
/etc/init.d/torque-mom start && \  
/etc/init.d/torque-scheduler start && \  
echo "Waiting 5 seconds to make sure the service starts..." && \  
sleep 5 && \  
qmgr -c "create queue batch queue_type=execution" && \  
qmgr -c "set server query_other_jobs = True" && \  
qmgr -c "set queue batch resources_max.ncpus=1" && \  
qmgr -c "set server default_queue=batch" && \  
echo "* Torque queue set" && \  
qmgr -c "set queue batch enabled=True" && \  
qmgr -c "set queue batch started=True" && \  
echo "* Torque queue started" && \  
qmgr -c "set queue batch resources_default.nodes=1" && \  
qmgr -c "set queue batch resources_default.walltime=3600" && \  
qmgr -c "set queue batch max_running=1" && \  
echo "* Torque queue parameters set" && \  
qmgr -c "set server scheduling=True" && \  
echo "* Torque scheduling started" && \  
qmgr -c "unset server acl_hosts" && \  
qmgr -c "set server acl_hosts=$HOSTNAME" && \  
echo "* Torque server ACL hosts set"  
  
## If the user 'root' should be allowed to submit, add also the next line  
# qmgr -c 's s acl_roots+=root@*' && \  
# echo "User 'root' now allowed to submit"  
## TODO: potentially decide if you want this to be a volume  
## You can do this also when running the container  
RUN mkdir /scratch  
  
# Expose SSH port  
EXPOSE 22  
### User to run job with the scheduler (root not allowed) ###  
# create an empty authorized_keys for user 'app', give right permissions  
RUN useradd --create-home --home /home/app \  
\--shell /bin/bash app && \  
usermod -L app && \  
chown app:app /scratch && \  
mkdir /home/app/.ssh && \  
touch /home/app/.ssh/authorized_keys && \  
chown -R app:app /home/app/.ssh && \  
chmod -R go= /home/app/.ssh  
  
## Put the script for the initial setup of the authorized_keys of the  
## app user  
COPY ./scripts/init_authorized_keys.sh /etc/my_init.d/init_authorized_keys.sh  
  
# So that supervisord log files go in /root and are not visible  
WORKDIR /root  
  
## Start services (torque)  
RUN mkdir -p /etc/service/torque_server && \  
mkdir -p /etc/service/torque_mom_scheduler  
  
COPY ./scripts/torque_server_run.sh /etc/service/torque_server/run  
COPY ./scripts/torque_mom_scheduler_run.sh
/etc/service/torque_mom_scheduler/run  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

