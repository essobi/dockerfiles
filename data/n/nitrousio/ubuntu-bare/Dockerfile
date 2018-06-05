FROM ubuntu-upstart:trusty  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
ENV NITROUS_IMAGE_VERSION 2  
ENV NITROUS_USERNAME nitrous  
ENV NITROUS_SSH_ENABLED true  
  
# Disable root password  
RUN passwd -l root  
  
# Create nitrous user and give sudo  
RUN \  
/bin/bash -c \  
'useradd --create-home -s /bin/bash $NITROUS_USERNAME && \  
adduser $NITROUS_USERNAME sudo && \  
mkdir -p /etc/sudoers.d && \  
echo $NITROUS_USERNAME ALL=NOPASSWD:ALL > /etc/sudoers.d/$NITROUS_USERNAME &&
\  
chmod 0440 /etc/sudoers.d/$NITROUS_USERNAME'  
  
RUN \  
mkdir -p /nitrous/init /nitrous/initonce && \  
touch /nitrous/dont_delete_this_dir  
  
RUN \  
rm /etc/legal && \  
rm /etc/update-motd.d/10-help-text  
  
ADD files/motd /etc/update-motd.d/00-header  
ADD files/nitrous_bootstrap.conf /etc/init/nitrous_bootstrap.conf  
ADD files/bootstrap.sh /nitrous/bootstrap.sh  
ADD files/dockerenv-inject /nitrous/dockerenv-inject  
ADD files/sshd_config /etc/ssh/sshd_config  
  
ADD files/nitrous-unison /nitrous/nitrous-unison  
ADD files/nitrous-watcher /nitrous/nitrous-watcher  
  
ADD files/init/0010-inject-env.sh /nitrous/init/0010-inject-env.sh  
  
ADD files/initonce/0010-generate-pw.sh /nitrous/initonce/0010-generate-pw.sh  
  
CMD ["/sbin/init", "--default-console", "none"]  

