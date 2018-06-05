# sshd  
#  
# Simple ssh server to sidecar on to another container, so that you can
inspect  
# the volumes with the "--volumes-from" option. E.g. if you have an already
running  
# container called "mycontainer" and you want to inspect the files in the
volumes:  
#  
# docker run --name mycontainer_sshd -d -p 3802:22 --volumes-from mycontainer
markgrimes/sshdaemon  
#  
# Then you can ssh on to port 3802 and inspect all the files. The password is
below  
# on the "chpasswd" line (this is intended as a debugging tool hence the
publicly  
# visible password).  
#  
# For a more complete (but much larger image size) example see  
# https://docs.docker.com/engine/examples/running_ssh_service/  
FROM alpine  
  
RUN apk add --no-cache dropbear openssh-sftp-server \  
&& mkdir /etc/dropbear  
  
RUN echo 'root:screencast' | chpasswd  
  
EXPOSE 22  
# Run dropbear creating host keys as required ("-R"); logging to stderr
("-E"); and  
# don't fork into the background ("-F") otherwise the container quits straight
away.  
CMD ["/usr/sbin/dropbear", "-R", "-E", "-F"]  

