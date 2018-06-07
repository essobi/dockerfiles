FROM yamashita109/base-jp:centos72trad  
  
MAINTAINER yamashita109  
  
RUN yum -y update \  
&& yum -y install mariadb-server \  
&& yum clean all \  
&& rm -rf /var/cache/yum/*;  
  
# To use systemctl is a proper way but it bring about  
# bus connection error of lacking needed privilege.  
# In addition, docker cannot use --privileged option while building,  
# therefore it handle settings manually.  
RUN ln -s /usr/lib/systemd/system/mariadb.service /etc/systemd/system/multi-
user.target.wants  
  
EXPOSE 3306  

