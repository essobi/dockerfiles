FROM justinxu/hadoop  
MAINTAINER Justin  
  
# Allow root login by ssh  
# Automatically accept public key  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config && \  
sed -i "s/^.*StrictHostKeyChecking.*$/StrictHostKeyChecking no/"
/etc/ssh/ssh_config  
  
# generate key pair  
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \  
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \  
chmod 0600 ~/.ssh/authorized_keys  
  
# Setting for Pseudo-Distributed Operation  
ADD pseudo/* "${HADOOP_CONF_DIR}"/  
  
CMD echo "root:password"|chpasswd && /etc/init.d/ssh start && /bin/bash  

