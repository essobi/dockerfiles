FROM gluster/gluster-centos  
MAINTAINER Clint Armstrong <clint@clintarmstrong.net>  
  
# ntpd is not needed, the time comes from the host  
# Disable root password auth, mount authorized keys for ssh authentication  
# Change the port back to default, I'm not worried about conflicts, docker
deals with that  
# using expose ports  
RUN systemctl disable ntpd.service && \  
sed -i 's/[#]*PermitRootLogin.*/PermitRootLogin prohibit-password/'
/etc/ssh/sshd_config&& \  
sed -i '/Port 2222/c\Port 22' /etc/ssh/sshd_config  

