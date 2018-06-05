FROM node:argon  
MAINTAINER Benjamin Kitt "benjamin@benjaminkitt.com"  
# Install and configure ssh  
RUN apt-get update && \  
apt-get -y install openssh-server pwgen sudo && \  
mkdir -p /var/run/sshd && \  
sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation yes/g"
/etc/ssh/sshd_config && \  
sed -i "s/PermitRootLogin without-password/PermitRootLogin no/g"
/etc/ssh/sshd_config  
  
# Set up environment variables  
ENV USER devbox  
ENV AUTHORIZED_KEY_FILE ./c9.id_rsa.pub  
  
# Add user account and include sudo group  
RUN useradd -ms /bin/bash -G sudo ${USER}  
WORKDIR /home/${USER}  
  
# Copy cloud9 public key to authorized_keys file  
COPY ["${AUTHORIZED_KEY_FILE}", "./.ssh/authorized_keys"]  
RUN chmod 600 ./.ssh/authorized_keys  
RUN chown ${USER}:${USER} -R ./.ssh  
  
# Install cloud9  
USER ${USER}  
RUN curl -L https://raw.githubusercontent.com/c9/install/master/install.sh |
bash  
  
# Expose ssh port and run sshd  
USER root  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

