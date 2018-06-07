# FROM ishidakazuya/paraview_5.1.2_mesa-llvm  
FROM ishidakazuya/paraview_5.1.2_mesa-llvm:latest  
  
# MAINTAINER is ishidakauya  
MAINTAINER ishidakazuya  
  
# Install OpenSSH server, OpenSSH clients and Supervisord  
RUN yum -y update \  
&& yum -y install openssh-server openssh-clients bind-utils epel-release \  
&& yum -y install supervisor \  
&& yum clean all \  
&& sed -i -e s/\\#Port\ 22/Port\ 22/ /etc/ssh/sshd_config \  
&& sed -i -e s@HostKey\ /etc/ssh/ssh_host_dsa_key@\\#HostKey\
/etc/ssh/ssh_host_dsa_key@ /etc/ssh/sshd_config \  
&& sed -i -e s@HostKey\ /etc/ssh/ssh_host_ecdsa_key@\\#HostKey\
/etc/ssh/ssh_host_ecdsa_key@ /etc/ssh/sshd_config \  
&& sed -i -e s@HostKey\ /etc/ssh/ssh_host_ed25519_key@\\#HostKey\
/etc/ssh/ssh_host_ed25519_key@ /etc/ssh/sshd_config \  
&& sed -i -e s/\\#PermitRootLogin\ yes/PermitRootLogin\ yes/
/etc/ssh/sshd_config \  
&& sed -i -e s/\\#PubkeyAuthentication\ yes/PubkeyAuthentication\ yes/
/etc/ssh/sshd_config \  
&& sed -i -e s/\\#PermitEmptyPasswords\ no/PermitEmptyPasswords\ yes/
/etc/ssh/sshd_config \  
&& ssh-keygen -t rsa -N "" -f /etc/ssh/ssh_host_rsa_key \  
&& mkdir /root/.ssh \  
&& touch /root/.ssh/authorized_keys \  
&& echo "StrictHostKeyChecking=no" > /root/.ssh/config \  
&& chmod 600 /root/.ssh/authorized_keys \  
&& chmod 600 /root/.ssh/config \  
&& chmod 700 /root/.ssh \  
&& passwd -d root \  
&& sed -i -e s/nodaemon=false/nodaemon=true/ /etc/supervisord.conf \  
&& echo "[program:sshd]" >> /etc/supervisord.d/sshd.ini \  
&& echo "command=/sbin/sshd -D" >> /etc/supervisord.d/sshd.ini \  
&& echo "stdout_logfile=/var/log/sshd_stdout.log" >>
/etc/supervisord.d/sshd.ini \  
&& echo "stderr_logfile=/var/log/sshd_stderr.log" >>
/etc/supervisord.d/sshd.ini \  
&& echo "stdout_logfile_maxbytes=1MB" >> /etc/supervisord.d/sshd.ini \  
&& echo "stderr_logfile_maxbytes=1MB" >> /etc/supervisord.d/sshd.ini \  
&& echo "autostart=true" >> /etc/supervisord.d/sshd.ini \  
&& echo "autorestart=false" >> /etc/supervisord.d/sshd.ini  
  
# EXPOSE Port 22  
EXPOSE 22  
# ENTRYPOINT is /usr/bin/supervisord  
ENTRYPOINT /usr/bin/supervisord -c /etc/supervisord.conf  

