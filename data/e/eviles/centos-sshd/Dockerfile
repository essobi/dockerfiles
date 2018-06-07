FROM centos:7  
  
RUN yum -y install openssh openssh-clients openssh-server python-setuptools \  
&& yum clean all \  
&& rm -rf /var/cache/yum/* \  
&& easy_install supervisor \  
&& ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa \  
&& ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa \  
&& ssh-keygen -A \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -i 's/session\s*required\s*pam_loginuid.so/session optional
pam_loginuid.so/g' /etc/pam.d/sshd \  
&& echo "[supervisord]" > /etc/supervisord.conf \  
&& echo "nodaemon=true" >> /etc/supervisord.conf \  
&& echo "[unix_http_server]" >> /etc/supervisord.conf \  
&& echo "file=/run/supervisord.sock" >> /etc/supervisord.conf \  
&& echo "chmod=0770" >> /etc/supervisord.conf \  
&& echo "[supervisorctl]" >> /etc/supervisord.conf \  
&& echo "serverurl=unix:///run/supervisord.sock" >> /etc/supervisord.conf \  
&& echo "[rpcinterface:supervisor]" >> /etc/supervisord.conf \  
&& echo
"supervisor.rpcinterface_factory=supervisor.rpcinterface:make_main_rpcinterface"
>> /etc/supervisord.conf \  
&& echo "[program:sshd]" >> /etc/supervisord.conf \  
&& echo "command=/usr/sbin/sshd -D" >> /etc/supervisord.conf  
  
EXPOSE 22  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
CMD ["/run.sh"]  

