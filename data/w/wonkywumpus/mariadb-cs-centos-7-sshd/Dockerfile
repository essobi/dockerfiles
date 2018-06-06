FROM centos:7  
# Install any needed packages specified in requirements.txt  
RUN yum -y update  
RUN yum -y install file  
RUN yum -y install sudo  
RUN yum -y install rsync  
RUN yum -y install iputils  
RUN yum -y install bind-utils  
RUN yum -y install vim  
RUN yum -y install boost  
RUN yum -y install expect perl perl-DBI openssl zlib file sudo libaio rsync
snappy net-tools perl-DBD-MySQL  
  
RUN yum -y install curl  
  
RUN yum -y install openssh-server  
RUN yum -y install openssh-clients  
  
RUN curl -o /root/mariadb-columnstore-1.0.10-1-centos7.x86_64.rpm.tar.gz
https://downloads.mariadb.com/ColumnStore/1.0.10/centos/x86_64/7/mariadb-
columnstore-1.0.10-1-centos7.x86_64.rpm.tar.gz  
  
RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa  
RUN ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa  
RUN echo 'root:m18#MDB' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
CMD ["/usr/sbin/sshd", "-D"]  
  
# SSH login fix. Otherwise user is kicked off after login  
# RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

