from tclavier/mailman2  
run apt-get update \  
&& apt-get install -y \  
ssh \  
vim \  
&& apt-get clean  
  
run sed -e 's/.*PasswordAuthentication.*/PasswordAuthentication no/g' -i
/etc/ssh/sshd_config  
add change_moderator_pw /usr/lib/mailman/bin/change_moderator_pw  
run chmod +x /usr/lib/mailman/bin/change_moderator_pw  
  
add default.cfg.erb /root/default.cfg.erb  
add listes /root/listes  
add reset_config /root/reset_config  
add reset_members /root/reset_members  
add reset_parents /root/reset_parents  
add reset_pwd /root/reset_pwd  
run chmod +x /root/reset_*  
  
add authorized_keys /root/.ssh/authorized_keys  
run chmod 600 /root/.ssh/authorized_keys  
run mkdir /var/run/sshd && \  
chmod 0755 /var/run/sshd  
  
cmd ["/usr/sbin/sshd", "-D"]  

