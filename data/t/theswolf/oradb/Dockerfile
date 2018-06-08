FROM theswolf/dockerbase  
  
ADD chkconfig /sbin/chkconfig  
ADD init.ora /  
ADD initXETemp.ora /  
  
RUN apt-get install -y libaio1 net-tools bc  
RUN ln -s /usr/bin/awk /bin/awk  
RUN mkdir /var/lock/subsys  
RUN chmod 755 /sbin/chkconfig  
#RUN ln -s /proc/mounts /etc/mtab  
  
RUM mkdir -p /tmp  
#ADD oracle-xe_11.2.0-1.0_amd64.deb /tmp/oracle-xe_11.2.0-1.0_amd64.deb  
RUN wget http://www.marco-gatti.com/debian/wheezy/unstable/oracle-
xe_11.2.0-1.0_amd64.deb -O /tmp/oracle-xe_11.2.0-1.0_amd64.deb  
RUN dpkg --install /tmp/oracle-xe_11.2.0-1.0_amd64.deb  
  
RUN mv /init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts  
RUN mv /initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts  
  
RUN printf 8080\\\n1521\\\noracle\\\noracle\\\ny\\\n | /etc/init.d/oracle-xe
configure  
  
RUN echo 'export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe' >>
/etc/bash.bashrc  
RUN echo 'export PATH=$ORACLE_HOME/bin:$PATH' >> /etc/bash.bashrc  
RUN echo 'export ORACLE_SID=XE' >> /etc/bash.bashrc  
  
EXPOSE 22  
EXPOSE 1521  
EXPOSE 8080  
ADD import.sh /  
ADD users.sql /  
ADD tables.sql /  
  
CMD sed -i -E "s/HOST = [^)]+/HOST = $HOSTNAME/g"
/u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora; \  
service oracle-xe start; \  
/usr/sbin/sshd -D  

