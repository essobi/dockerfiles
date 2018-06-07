FROM alpine:latest  
LABEL Vendor="Codesim, LLC"  
LABEL License=GPLv2  
LABEL Description="Simple SFTP server. Requires three mount points: /hostkeys,
/etc/passwd and /home, where /hostkeys contains host-generated SSH keys that
will persist between container restarts, /etc/passwd contains root, sshd, and
each user that will have access to sftp into the container, and where /home is
mapped to a host directory containing a subdirectory (also owned and writable
only by root) for each sftp user defined in /etc/passwd. For those home
subdirectories, ensure there is a .ssh subdirectory containing an
authorized_keys file with the sftp user's public key. Also, create any sftp-
writable subdirectories within each sftp user's home directory, if the sftp
user will need access to write files. See https://github.com/jertel/sftpimg
for more information."  
  
COPY start.sh /  
COPY start-debug.sh /  
  
RUN apk update && \  
apk add openssh-server && \  
sed -i -e 's/\/usr\/lib\/ssh\/sftp-server/internal-sftp/' /etc/ssh/sshd_config
&& \  
echo "PermitRootLogin no" >> /etc/ssh/sshd_config && \  
echo "PasswordAuthentication no" >> /etc/ssh/sshd_config && \  
echo "Protocol 2" >> /etc/ssh/sshd_config && \  
echo "ChrootDirectory %h" >> /etc/ssh/sshd_config && \  
echo "ForceCommand internal-sftp" >> /etc/ssh/sshd_config && \  
echo "AllowTcpForwarding no" >> /etc/ssh/sshd_config && \  
echo "Port 2200" >> /etc/ssh/sshd_config && \  
echo "HostKey /hostkeys/ssh_host_rsa_key" >> /etc/ssh/sshd_config && \  
echo "HostKey /hostkeys/ssh_host_dsa_key" >> /etc/ssh/sshd_config && \  
echo "HostKey /hostkeys/ssh_host_ecdsa_key" >> /etc/ssh/sshd_config && \  
echo "HostKey /hostkeys/ssh_host_ed25519_key" >> /etc/ssh/sshd_config && \  
echo "Welcome to SFTPImg" > /etc/motd && \  
chmod u+x /start.sh && \  
chmod u+x /start-debug.sh  
  
EXPOSE 2200  
ENTRYPOINT /start.sh

