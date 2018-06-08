#--------- Generic stuff all our Dockerfiles should start with so we get
caching ------------  
FROM ubuntu:14.04  
RUN export DEBIAN_FRONTEND=noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
# socat can be used to proxy an external port and make it look like it is
local  
RUN apt-get -y update; apt-get -y install ca-certificates openssh-server pwgen
rsync  
RUN mkdir /var/run/sshd  
  
# Ubuntu 14.04 by default only allows non pwd based root login  
# We disable that but also create an .ssh dir so you can copy  
# up your key. NOTE: This is not a particularly robust setup  
# security wise and we recommend to NOT expose ssh as a public  
# service.  
#RUN rpl "PermitRootLogin without-password" "PermitRootLogin yes"
/etc/ssh/sshd_config  
#RUN mkdir /root/.ssh  
#RUN chmod o-rwx /root/.ssh  
# Create a non privileged user 'realtime'  
# You will be able to get the user credentials by doing  
# docker cp <container-id>/<path> <local filesystem path>  
# i.e. docker cp inasafe-realtime-sftp:/etc/realtime.credentials
realtime.credentials  
RUN REALTIME_PASSWORD=`pwgen -c -n -1 12`; echo "User: realtime Password:
$REALTIME_PASSWORD" > /credentials && useradd -m -d /home/realtime -s
/bin/bash realtime; echo "realtime:$REALTIME_PASSWORD" | chpasswd; echo
"Realtime user password $REALTIME_PASSWORD"  
  
#-------------Application Specific Stuff
----------------------------------------------------  
# Open port 22 so linked containers can see it  
EXPOSE 22  
# Called on first run of docker  
ADD entry-point.sh /entry-point.sh  
RUN chmod 0755 /entry-point.sh  
  
CMD /entry-point.sh  
  

