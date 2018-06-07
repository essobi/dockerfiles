FROM docker:dind  
  
RUN \  
apk add --update bash openssh sudo openjdk7-jre-base git supervisor && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /var/log/supervisor  
ADD supervisord.conf /etc/supervisord.conf  
  
RUN \  
rc-update add sshd && \  
rc-status && \  
touch /run/openrc/softlevel && \  
sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication yes/'
/etc/ssh/sshd_config && \  
sed -i 's/^#PermitUserEnvironment no/PermitUserEnvironment yes/'
/etc/ssh/sshd_config && \  
ssh-keygen -A -N ''  
  
RUN \  
adduser -D -s /bin/bash farmer && \  
echo -n 'farmer:farmer' | chpasswd && \  
mkdir /home/farmer/.ssh && \  
echo 'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' >>
/home/farmer/.ssh/environment && \  
echo 'farmer ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/farmer  
  
EXPOSE 22  
ENTRYPOINT []  
CMD ["supervisord"]  

