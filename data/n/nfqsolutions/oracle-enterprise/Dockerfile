FROM nfqsolutions/centos:7  
  
MAINTAINER solutions@nfq.com  
  
# Ficheros que se utilizaran en la instalacion y en el funcionamiento normal  
COPY oracle_installation /oracle_installation  
RUN chmod -R 777 /oracle_installation && \  
chmod a+x /oracle_installation/*.sh && \  
sed -i -e 's/\r$//' /oracle_installation/*.sh && \  
mv /oracle_installation/new_database.sh /oracle_installation/new_database && \  
mv /oracle_installation/delete_database.sh
/oracle_installation/delete_database  
# Instalacion previa  
RUN yum install -y binutils compat-libstdc++-33 compat-libstdc++-33.i686 ksh
elfutils-libelf \  
elfutils-libelf-devel glibc glibc-common glibc-devel gcc gcc-c++ libaio
libaio.i686 libaio-devel \  
libaio-devel.i686 libgcc libstdc++ libstdc++.i686 libstdc++-devel
libstdc++-devel.i686 make sysstat \  
unixODBC unixODBC-devel wget tar && \  
yum clean all && \  
rm -rf /var/lib/{cache,log} /var/log/lastlog  
# Configurando usuarios  
RUN useradd oracle  
RUN groupadd -g 200 oinstall && groupadd -g 201 dba && \  
usermod -a -G root,oinstall,dba oracle && \  
echo "root:solutions" | chpasswd && \  
echo "oracle:solutions" | chpasswd && \  
echo "oracle ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
sed -i "s/Defaults requiretty/#Defaults requiretty/g" /etc/sudoers && \  
sed -i "s/pam_namespace.so/pam_namespace.so\nsession required pam_limits.so/g"
/etc/pam.d/login && \  
mkdir -p -m 777 /u01  
# Configurando sysctl  
RUN echo "net.ipv4.ip_local_port_range = 9000 65500" > /etc/sysctl.conf && \  
echo "fs.file-max = 6815744" >> /etc/sysctl.conf && \  
echo "kernel.shmall = 10523004" >> /etc/sysctl.conf && \  
echo "kernel.shmmax = 6465333657" >> /etc/sysctl.conf && \  
echo "kernel.shmmni = 4096" >> /etc/sysctl.conf && \  
echo "kernel.sem = 250 32000 100 128" >> /etc/sysctl.conf && \  
echo "net.core.rmem_default=262144" >> /etc/sysctl.conf && \  
echo "net.core.wmem_default=262144" >> /etc/sysctl.conf && \  
echo "net.core.rmem_max=4194304" >> /etc/sysctl.conf && \  
echo "net.core.wmem_max=1048576" >> /etc/sysctl.conf && \  
echo "fs.aio-max-nr = 1048576" >> /etc/sysctl.conf  
# Configurando limits files  
RUN echo "oracle soft nproc 2047" >> /etc/security/limits.conf && \  
echo "oracle hard nproc 16384" >> /etc/security/limits.conf && \  
echo "oracle soft nofile 1024" >> /etc/security/limits.conf && \  
echo "oracle hard nofile 65536" >> /etc/security/limits.conf  
  
USER oracle  
  
# Variables de entorno  
ENV ORACLE_BASE=/u01/app/oracle \  
ORACLE_SID=ORA \  
ORACLE_HOME=/u01/app/oracle/product/11.2.0/dbhome_1 \  
ORACLE_INVENTORY=/u01/app/oraInventory \  
ORACLE_HOME_LISTNER=/u01/app/oracle/product/11.2.0/dbhome_1 \  
LD_LIBRARY_PATH=/u01/app/oracle/product/11.2.0/dbhome_1/lib:/lib:/usr/lib \  
CLASSPATH=/u01/app/oracle/product/11.2.0/dbhome_1/jlib:\/u01/app/oracle/product/11.2.0/dbhome_1/rdbms/jlib
\  
NLS_LANG=AMERICAN.AL32UTF8 \  
NLS_DATE_FORMAT="YYYY-MM-DD HH24:MI:SS" \  
PATH=$PATH:/usr/sbin:/u01/app/oracle/product/11.2.0/dbhome_1/bin:/oracle_installation  
# Volumenes para el docker  
VOLUME /u01  
# Puerto de salida del docker  
EXPOSE 1521  
EXPOSE 8080  
  
# Configuracion supervisor  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]

