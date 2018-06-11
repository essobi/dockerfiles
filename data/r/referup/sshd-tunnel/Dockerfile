FROM pataquets/sshd-tunnel  
  
RUN \  
grep -e "^PasswordAuthentication no$" /etc/ssh/sshd_config && \  
grep -e "^PermitEmptyPasswords no$" /etc/ssh/sshd_config && \  
grep -e "^X11Forwarding no$" /etc/ssh/sshd_config \  
&& \  
echo "" | tee -a /etc/ssh/sshd_config && \  
echo "# Allowed tunnel forwardings" | tee -a /etc/ssh/sshd_config && \  
echo "PermitOpen mysql:3306 mysql-slave:3306 mongo:27017" | tee -a
/etc/ssh/sshd_config && \  
grep -e "^PermitOpen" /etc/ssh/sshd_config \  
&& \  
nl /etc/ssh/sshd_config  

