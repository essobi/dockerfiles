# Building  
#  
# This Dockerfile builds ubuntu image with sshd.  
# It requires at least one public key to be present in public-keys directory.  
# Usually you can find you public keys in $HOME/.ssh/*.pub  
# So you can copy them with command:  
# cp $HOME/.ssh/*.pub public-keys/  
FROM ubuntu  
MAINTAINER Dawid Sklodowski  
  
RUN apt-get -q -y update  
RUN apt-get -q -y install openssh-server  
  
RUN echo "%sudo ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/nopasswd  
  
RUN useradd --create-home --shell /bin/bash --user-group --groups adm,sudo
ubuntu  
RUN mkdir /home/ubuntu/.ssh  
COPY public-keys /home/ubuntu/public-keys  
  
# Check if there are any keys in public-keys. Exit with message if there are
none.  
RUN test $(ls /home/ubuntu/public-keys/* | wc -l) -gt 0 || (echo "\n\n No keys
present in public-keys.\n Please copy your public key to public-keys.\n\n" &&
exit 1)  
  
RUN cat /home/ubuntu/public-keys/* > /home/ubuntu/.ssh/authorized_keys  
RUN rm -rf /home/ubuntu/public-keys  
RUN mkdir /var/run/sshd  
  
RUN chown -R ubuntu:ubuntu /home/ubuntu/.ssh  
EXPOSE 22  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]  

