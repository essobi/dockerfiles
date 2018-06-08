# Dockerfile to create an Oracle Service  
# Origin project from: Alexei Ledenev <alexei.led@gmail.com>  
FROM buildpack-deps:trusty-curl  
  
MAINTAINER Rafael Dutra <rafael.dutra.gimenez@agcocorp.com>  
  
COPY system-config/chkconfig /sbin/chkconfig  
COPY oracle-config/init.ora /  
COPY oracle-config/initXETemp.ora /  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libaio1 net-tools bc unixodbc && \  
apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/awk /bin/awk && \  
ln -sf /proc/mounts /etc/mtab && \  
mkdir /var/lock/subsys && \  
> /var/lock/subsys/listener && \  
chmod 755 /sbin/chkconfig  
  
COPY oracle-shm /etc/init.d/oracle-shm  
RUN chmod 755 /etc/init.d/oracle-shm && \  
/etc/init.d/oracle-shm start  
  
COPY ./oracle-pkg /tmp  
RUN cat /tmp/oracle-xe_11.2.0-1.0_amd64.deba* > /tmp/oracle-
xe_11.2.0-1.0_amd64.deb && \  
dpkg --install /tmp/oracle-xe_11.2.0-1.0_amd64.deb && \  
rm /tmp/oracle-xe_11.2.0-1.0_amd64.deb  
  
RUN mv /init.ora /u01/app/oracle/product/11.2.0/xe/config/scripts && \  
mv /initXETemp.ora /u01/app/oracle/product/11.2.0/xe/config/scripts  
  
RUN printf 8080\\\n1521\\\noracle\\\noracle\\\ny\\\n | /etc/init.d/oracle-xe
configure >/dev/null  
  
RUN echo 'export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe' >>
/etc/bash.bashrc && \  
echo 'export PATH=$ORACLE_HOME/bin:$PATH' >> /etc/bash.bashrc && \  
echo 'export ORACLE_SID=XE' >> /etc/bash.bashrc  
  
# Oracle data volume  
VOLUME /usr/lib/oracle/xe/oradata/XE  
# Oracle volume for init SQL scripts  
#VOLUME /etc/oracle-environment  
EXPOSE 1521 8080  
COPY oracle.sh /  
RUN chmod 755 /oracle.sh  
RUN mkdir /etc/oracle-environment  
COPY oracle-environment/*.sql /etc/oracle-environment/  
  
CMD /oracle.sh  

