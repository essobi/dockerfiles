FROM centos:centos6.6  
MAINTAINER Paras Patel(parasprince2001@gmail.com)  
WORKDIR /docker  
RUN yum install -y openssh-server wget telnet nc sudo \  
yum clean all && \  
sed -i -e "s:^UsePAM yes$:#UsePAM yes:" /etc/ssh/sshd_config && \  
sed -i -e "s:^#UsePAM no$:UsePAM no:" /etc/ssh/sshd_config && \  
useradd -d /home/leofs -m -s /bin/bash leofs && \  
echo leofs:leofs | chpasswd;echo 'leofs ALL=(ALL) NOPASSWD:ALL' >>
/etc/sudoers && \  
rpm -ivh https://github.com/leo-
project/leofs/releases/download/1.2.21/leofs-1.2.21-1.el6.x86_64.rpm && \  
mkdir /usr/local/leofs/bin && \  
touch /usr/local/leofs/bin/start_leofs.sh && \  
chmod 755 /usr/local/leofs/bin/start_leofs.sh && \  
echo '#!/usr/bin/env sh' >> /usr/local/leofs/bin/start_leofs.sh && \  
echo '/usr/local/leofs/1.2.21/leo_manager_0/bin/leo_manager start' >>
/usr/local/leofs/bin/start_leofs.sh && \  
echo '/usr/local/leofs/1.2.21/leo_manager_1/bin/leo_manager start' >>
/usr/local/leofs/bin/start_leofs.sh && \  
echo '/usr/local/leofs/1.2.21/leo_storage/bin/leo_storage start' >>
/usr/local/leofs/bin/start_leofs.sh && \  
echo 'sleep 30' >> /usr/local/leofs/bin/start_leofs.sh && \  
echo 'leofs-adm start' >> /usr/local/leofs/bin/start_leofs.sh && \  
echo '/usr/local/leofs/1.2.21/leo_gateway/bin/leo_gateway start' >>
/usr/local/leofs/bin/start_leofs.sh && \  
echo '/etc/init.d/sshd start' >> /usr/local/leofs/bin/start_leofs.sh && \  
echo 'echo "LeoFS is ready!!"' >> /usr/local/leofs/bin/start_leofs.sh && \  
echo 'tail -f /dev/null' >> /usr/local/leofs/bin/start_leofs.sh  
EXPOSE 22 8080 10010 10011 10020 10021  
CMD ["/usr/local/leofs/bin/start_leofs.sh"]  

