FROM debian  
MAINTAINER Alexander Ustimenko "http://ustimen.co/"  
EXPOSE 22  
# Build args  
COPY ARG.sh /usr/bin/ARG  
COPY build.args*.sh /etc/  
  
RUN \  
apt-get --quiet=2 update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get --assume-yes --no-install-recommends --quiet=2 install \  
openssh-server && \  
apt-get clean && \  
rm --recursive --force /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /etc/ssh  
  
RUN \  
echo "root:$(ARG ROOT_PASSWORD)" | chpasswd && \  
echo "Root password changed" && \  
\  
sed --in-place 's/^\\(PermitRootLogin\|UsePAM\|UseDNS\\)/#\1/' sshd_config &&
\  
echo "" >> sshd_config && \  
echo "# Custom changes from `date`" >> sshd_config && \  
echo "PermitRootLogin $(ARG SSHD_CONFIG_PERMIT_ROOT_LOGIN)" >> sshd_config &&
\  
echo "UsePAM $(ARG SSHD_CONFIG_USE_PAM)" >> sshd_config && \  
echo "UseDNS $(ARG SSHD_CONFIG_USE_DNS)" >> sshd_config && \  
echo "SSH daemon config updated" && \  
\  
rm /usr/bin/ARG /etc/build.args*.sh  
  
# This will create all required directories/files  
RUN service ssh start  
  
CMD [ \  
# Path to OpenSSH SSH daemon  
"/usr/sbin/sshd", \  
# will not detach and does not become a daemon  
"-D", \  
# will send the output to the standard error instead of the system log  
"-e" \  
]  

