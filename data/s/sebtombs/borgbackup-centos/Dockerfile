FROM centos:latest  
MAINTAINER "Mark D-B" <dh1@sebtombs.com>  
  
RUN yum -y update  
RUN yum -y install epel-release  
  
# Fedora dependency list from BorgBackup web site  
RUN yum -y install python34 python34-devel python34-pip  
# RUN yum install -y python3-virtualenv - this seems to be missing from EPEL.
It doesn't seem to stop Borg installing  
RUN yum -y install openssl-devel openssl  
RUN yum -y install libacl-devel libacl  
RUN yum -y install lz4-devel  
RUN yum -y install gcc gcc-c++  
RUN yum -y install fuse-devel fuse pkgconfig  
  
# We need ssh client for Borg to connect to remote repositories  
RUN yum -y install openssh-clients  
  
# Include pv in case the user wants to do bandwidth limiting  
RUN yum -y install pv  
  
# Now install BorgBackup - we don't use VirtualEnv as we are root in the
container anyway  
RUN pip3 install borgbackup  
#or, if we want FUSE  
#RUN pip3 install borgbackup[fuse]  
# Bring in BorgWeb - contrary to the web site, it appears to be in the pip
repo rather than needing a git clone  
RUN pip3 install borgweb  
  
# And BorgMatic to manage creation and pruning of backups  
RUN pip3 install borgmatic  
  
# Now, bring in our mechanisms for the containerised backup  
# Rather than updating the crontab every time the user modifies the backup
criteria,  
# we instead call a script every few minutes  
# TODO!  
# Outstanding issues/problems  
# a) Rockstor can (and, in most cases will), be configured to have snapshots
visible inside shares  
# The naming of snapshots is user defined. We do *not* want Borg to back up
all the snapshots  
# as this will waste space. How do we know what to exclude?  
# b) The user may not want to back up everything in /mnt2. How do we handle
that?  
# Expose port (Temporary, for testing only!)  
EXPOSE 22  
# Copying is not going to work here - we need the keys to be defined on the
appliance, not in the Dockerfile  
#COPY sshkeys/* /root/.ssh/  
# copy the script used for rate limiting  
COPY pv-wrapper.sh /root/pv-wrapper.sh  
  
ENTRYPOINT ["/usr/bin/borgweb"]  

