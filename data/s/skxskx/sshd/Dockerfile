#  
# Build it like so:  
#  
# root@host~# docker build -t=skxskx/sshd .  
#  
# Launch the generated image like so:  
#  
# root@host~# docker run -d -p 2222:22 skxskx/sshd  
#  
# Connect like so, with the root password being "mypasswd".  
#  
# $ ssh -p 2222 root@localhost  
#  
# Steve  
# --  
#  
#  
# From this base-image / starting-point  
#  
FROM ubuntu  
  
#  
# Authorship  
#  
MAINTAINER steve@steve.org.uk  
  
#  
# Update apt  
#  
RUN apt-get update -q -q  
  
#  
# Install runit, which will monitor our SSH instance.  
#  
RUN apt-get install runit --yes --force-yes  
  
#  
# Install SSH  
#  
RUN apt-get install openssh-server openssh-client --yes --force-yes  
  
#  
# Setup a root password; simple enough to remember, but hard enough that  
# it won't be cracked immediately. (ha!)  
#  
RUN echo "root:mypasswd" | chpasswd  
  
#  
# Expose the SSH port  
#  
EXPOSE 22  
#  
# Now make sure that runit will launch SSHD, via runit.  
#  
# NOTE: Remember runit will launch /etc/service/sshd/run  
#  
RUN mkdir /etc/service/sshd  
RUN /bin/echo -e '#!/bin/sh' > /etc/service/sshd/run  
RUN /bin/echo -e "mkdir -p /var/run/sshd" >> /etc/service/sshd/run  
RUN /bin/echo -e 'exec /usr/sbin/sshd -D' >> /etc/service/sshd/run  
  
#  
# Make sure our run-script is executable.  
#  
RUN chown root.root /etc/service/sshd/run  
RUN chmod 755 /etc/service/sshd/run  
  
#  
# Finally launch runit.  
#  
ENTRYPOINT ["/usr/sbin/runsvdir-start"]  
  

