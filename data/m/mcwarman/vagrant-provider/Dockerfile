FROM alpine  
MAINTAINER Matthew Warman <mcwarman@gmail.com>  
RUN apk add --update openssh sudo \  
&& rm -rf /tmp/* /var/cache/apk/*  
RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key  
RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
  
RUN adduser -D -s /bin/ash vagrant  
RUN passwd -d vagrant vagrant  
RUN echo 'vagrant ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/vagrant  
RUN chmod 440 /etc/sudoers.d/vagrant  
  
RUN mkdir -p /home/vagrant/.ssh  
RUN chmod 700 /home/vagrant/.ssh  
ADD
https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant.pub
/home/vagrant/.ssh/authorized_keys  
RUN chmod 600 /home/vagrant/.ssh/authorized_keys  
RUN chown -R vagrant:vagrant /home/vagrant/.ssh  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd","-D"]  

