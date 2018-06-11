FROM pataquets/sshd:xenial  
  
# Add and configure built-in 'tunnel' user with:  
# - No password.  
# - Having /bin/false as shell.  
# - Empty ~/.ssh/authorized_keys file.  
RUN \  
useradd --create-home --shell /bin/false tunnel && \  
mkdir -vp --mode=700 /home/tunnel/.ssh/ && \  
touch /home/tunnel/.ssh/authorized_keys && \  
chown -vR tunnel:tunnel /home/tunnel/.ssh && \  
ls -ARl /home/tunnel/  
  
RUN \  
echo "PermitTTY no" | tee -a /etc/ssh/sshd_config && \  
grep -e "^PermitTTY no$" /etc/ssh/sshd_config \  
&& \  
sed -i "s/^\\#PasswordAuthentication yes$/PasswordAuthentication no/g"
/etc/ssh/sshd_config && \  
grep -e "^PasswordAuthentication no$" /etc/ssh/sshd_config \  
&& \  
sed -i "s/X11Forwarding yes/X11Forwarding no/g" /etc/ssh/sshd_config && \  
grep -e "^X11Forwarding no$" /etc/ssh/sshd_config \  
&& \  
nl /etc/ssh/sshd_config \  
&& \  
grep -e "^PermitEmptyPasswords no$" /etc/ssh/sshd_config  

