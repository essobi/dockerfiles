# Dockerfile for Spoke-Base  
#  
# This Spoke-Base Dockerfile adds a required package for Spoke container  
# management in the Radial topology. Supervisor is used as the main interface  
# for `docker attach` as well as for managing the running process contained  
# therein. Installation is done here to allow for the Spoke container to be
only  
# focused on the application code.  
FROM radial/distro:us-west-1  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Keep upstart from throwing errors  
RUN dpkg-divert --local \--rename --add /sbin/initctl &&\  
ln -sf /bin/true /sbin/initctl  
  
# Update system (usually very small), install default packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update &&\  
apt-get -qyV upgrade &&\  
apt-get -qyV install \  
supervisor &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
# Add our universal Spoke ENTRYPOINT  
COPY /spoke-entrypoint.sh /spoke-entrypoint.sh  
  
# Not meant for running by itself.  
ENTRYPOINT /bin/false  
  
# Update System again before actual build  
ONBUILD ENV DEBIAN_FRONTEND noninteractive  
ONBUILD RUN apt-get -q update &&\  
apt-get -qyV upgrade &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
# By default, the contents of '/data' is owned by root (set in the  
# radial/hub-base Dockerfile) with 755 folder permissions. If this folder, or  
# any of it's subfolders, need to have different permissions or ownership, it  
# must be done in the entrypoint.sh script for that spokes application (the
one  
# started in the Supervisor .ini file). Since '/data' is a volume container,  
# this cannot be done in any of the Dockerfiles themselves. Remember to  
# actually run your application as the appropriate user. You can set this  
# information in your Supervisor .ini file for this program located in  
# '/config/supervisor/conf.d'.  
# Supervisor itself will be run as root regardless.  
# On the resulting Spoke container, this ENTRYPOINT script will:  
# 1) Create a unique folder for all our logs based on our container name  
# 2) Start the supervisor daemon  
# 3) Start this Spoke's main app group and  
# 4) Show the combined output of the app and Supervisor  
ONBUILD ENTRYPOINT ["/spoke-entrypoint.sh"]  

