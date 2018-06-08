FROM ubuntu:14.04.1  
# first line must be base image in FROM for automatic build!  
#  
# Official Ubuntu base image  
#  
# Oracle Database Express Edition 11g Release 2  
# http://www.oracle.com/technetwork/licenses/database-11g-express-
license-459621.html  
#  
# build context size: 317MB  
# image size: 2544MB (clear database)  
#  
MAINTAINER Bjoern Lakeberg <bjoern.lakeberg@technik-emden.de>  
  
# add trailing / tells add command treat it as a folder!  
ADD chkconfig /sbin/chkconfig/  
ADD init.ora /tmp/  
ADD initXETemp.ora /tmp/  
ADD oracle-xe-11.2.0-1.0.x86_64.rpm /tmp/  
  
# own scripts and sql for creating database and pump data  
ADD ownstartdb.sh /tmp/  
ADD ownstopdb.sh /tmp/  
  
# load packages and install ssh server  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:admin' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
# load packages and prepare to install oracle  
RUN apt-get install -y libaio1 net-tools bc alien  
RUN ln -s /usr/bin/awk /bin/awk  
RUN mkdir /var/lock/subsys  
RUN chmod 755 /sbin/chkconfig /tmp/ownstartdb.sh /tmp/ownstopdb.sh  
  
# convert red-hat to ubuntu package and install oracle  
RUN alien --scripts --install /tmp/oracle-xe-11.2.0-1.0.x86_64.rpm  
  
# move scripts to oracle config/scripts directory  
RUN mv /tmp/init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts  
RUN mv /tmp/initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts  
RUN mv /tmp/ownstartdb.sh /u01/app/oracle/product/11.2.0/xe/config/scripts  
RUN mv /tmp/ownstopdb.sh /u01/app/oracle/product/11.2.0/xe/config/scripts  
  
# create ports and user credentials for oracle in init.d  
RUN printf 8080\\\n1521\\\noracle\\\noracle\\\ny\\\n | /etc/init.d/oracle-xe
configure  
  
# export oracle standard variables (home, path, sid) to bash  
RUN echo 'export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe' >>
/etc/bash.bashrc  
RUN echo 'export PATH=$ORACLE_HOME/bin:$PATH' >> /etc/bash.bashrc  
RUN echo 'export ORACLE_SID=XE' >> /etc/bash.bashrc  
  
# clean up install file  
RUN rm -f /tmp/oracle-xe-11.2.0-1.0.x86_64.rpm  
  
# define and expose ports for ssh and oracle jdbc  
EXPOSE 22  
EXPOSE 1521  
# change hostname for oracle network listener, start ssh and database from own
script  
CMD sed -i -E "s/HOST = [^)]+/HOST = $HOSTNAME/g"
/u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora; \  
/u01/app/oracle/product/11.2.0/xe/config/scripts/ownstartdb.sh; \  
/usr/sbin/sshd -D

