# FROM ishidakazuya/sage2  
FROM ishidakazuya/sage2:latest  
  
# MAINTAINER is ishidakazuya  
MAINTAINER ishidakazuya  
  
# Install OpenSSH server and Supervisord  
RUN apt-get -y update \  
&& apt-get -y install openssh-server supervisor \  
&& apt-get clean \  
&& sed -i -e s@HostKey\ /etc/ssh/ssh_host_dsa_key@\\#HostKey\
/etc/ssh/ssh_host_dsa_key@ /etc/ssh/sshd_config \  
&& sed -i -e s@HostKey\ /etc/ssh/ssh_host_ecdsa_key@\\#HostKey\
/etc/ssh/ssh_host_ecdsa_key@ /etc/ssh/sshd_config \  
&& sed -i -e s@HostKey\ /etc/ssh/ssh_host_ed25519_key@\\#HostKey\
/etc/ssh/ssh_host_ed25519_key@ /etc/ssh/sshd_config \  
&& sed -i -e s/PermitRootLogin\ prohibit-password/PermitRootLogin\ yes/
/etc/ssh/sshd_config \  
&& sed -i -e s/StrictModes\ yes/StrictModes\ no/ /etc/ssh/sshd_config \  
&& sed -i -e s/\PermitEmptyPasswords\ no/PermitEmptyPasswords\ yes/
/etc/ssh/sshd_config \  
&& sed -i -e s/UsePAM\ yes/UsePAM\ no/ /etc/ssh/sshd_config \  
&& ssh-keygen -y -t rsa -N "" -f /etc/ssh/ssh_host_rsa_key \  
&& mkdir /var/run/sshd \  
&& mkdir /root/.ssh \  
&& touch /root/.ssh/authorized_keys \  
&& chmod 600 /root/.ssh/authorized_keys \  
&& chmod 700 /root/.ssh \  
&& passwd -d root \  
&& echo "[program:sshd]" >> /etc/supervisor/conf.d/sshd.ini \  
&& echo "command=/usr/sbin/sshd -D" >> /etc/supervisor/conf.d/sshd.ini \  
&& echo "stdout_logfile=/var/log/sshd_stdout.log" >>
/etc/supervisor/conf.d/sshd.ini \  
&& echo "stderr_logfile=/var/log/sshd_stderr.log" >>
/etc/supervisor/conf.d/sshd.ini \  
&& echo "stdout_logfile_maxbytes=1MB" >> /etc/supervisor/conf.d/sshd.ini \  
&& echo "stdout_logfile_maxbytes=1MB" >> /etc/supervisor/conf.d/sshd.ini \  
&& echo "autostart=true" >> /etc/supervisor/conf.d/sshd.ini \  
&& echo "autorestart=false" >> /etc/supervisor/conf.d/sshd.ini \  
&& touch /var/run/supervisor.sock \  
&& chmod 777 /var/run/supervisor.sock  
  
# ADD supervisord.conf  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
  
# EXPOSE Port 22  
EXPOSE 22  
# ENTRYPOINT is /usr/bin/supervisord  
ENTRYPOINT /usr/bin/supervisord -c /etc/supervisor/supervisord.conf  
  

