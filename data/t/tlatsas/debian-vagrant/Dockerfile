FROM debian:latest  
MAINTAINER Tasos Latsas "tlatsas@kodama.gr"  
RUN useradd --create-home --shell /bin/bash vagrant  
RUN echo root:vagrant | chpasswd  
RUN echo vagrant:vagrant | chpasswd  
  
ADD
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub \  
/home/vagrant/.ssh/authorized_keys  
RUN chown -R vagrant:vagrant /home/vagrant/.ssh  
RUN chmod 0600 /home/vagrant/.ssh/authorized_keys  
RUN chmod 0700 /home/vagrant/.ssh  
  
RUN apt-get update \  
&& apt-get install -y openssh-server sudo wget curl puppet \  
&& apt-get clean  
  
RUN sed --regexp-extended --in-place \  
's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' \  
/etc/pam.d/sshd  
  
ADD sudoers.d/01_vagrant /etc/sudoers.d/  
RUN chmod 0400 /etc/sudoers.d/01_vagrant  
  
RUN mkdir /var/run/sshd  
CMD ["/usr/sbin/sshd", "-D", "-e"]  
EXPOSE 22  

