FROM justinxu/hadoop-pseudo  
  
MAINTAINER Justin  
  
# Setting for Pseudo-Distributed-yarn Operation  
ADD pseudo/yarn/* "${HADOOP_CONF_DIR}"/  
  
CMD echo "root:password"|chpasswd && /etc/init.d/ssh start && /bin/bash  

