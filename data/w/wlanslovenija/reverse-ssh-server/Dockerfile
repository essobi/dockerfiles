FROM tozd/runit  
  
EXPOSE 27932/tcp  
  
VOLUME /etc/ssh/keys  
VOLUME /readonly/files  
  
RUN apt-get -q -q update && \  
apt-get --no-install-recommends --yes --force-yes install openssh-server && \  
mkdir -p /readonly && \  
chown -R root:root /readonly && \  
chmod 555 /readonly && \  
echo "/bin/true" >> /etc/shells && \  
useradd --home-dir /readonly \--shell /bin/true \--no-create-home reverse && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
sed 's@session\s*optional\s*pam_motd.so@#@g' -i /etc/pam.d/sshd && \  
rm /etc/ssh/ssh_host_*  
  
ADD ./etc /etc  
  

