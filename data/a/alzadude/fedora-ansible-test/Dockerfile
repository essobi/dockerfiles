FROM fedora:23  
MAINTAINER http://github.com/alzadude/docker-fedora-ansible-test  
  
# Install packages and set up sshd  
RUN dnf -q -y install openssh-server pwgen sudo  
# Install python 2 and dependencies for ansible modules  
RUN dnf -q -y install python2 python2-dnf libselinux-python  
# Install of python-yumdaemon is temporary, it can be removed when yum module
is no longer used in ansible tasks  
RUN dnf -q -y install python-yumdaemon  
RUN dnf clean all  
#RUN sed -i 's/#*UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g'
/etc/ssh/sshd_config  
#RUN sed -i 's/#*UseDNS.*/UseDNS no/g' /etc/ssh/sshd_config  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]  
  

