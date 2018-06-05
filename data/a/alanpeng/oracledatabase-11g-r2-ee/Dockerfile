FROM oraclelinux  
MAINTAINER peng.alan@gmail.com  
  
ADD install /install  
  
ENV ORACLE_BASE=/u01/app/oracle  
ENV ORACLE_HOME=$ORACLE_BASE/product/11.2.0/db_1  
ENV PATH=$ORACLE_HOME/bin:$PATH  
ENV ORACLE_HOME_LISTNER=$ORACLE_HOME  
ENV ORACLE_SID=orcl  
ENV ORACLE_SRC_INSTALL_DIR=/install/database  
ENV TZ=Etc/GMT-3  
  
#Prereq  
RUN yum -y install oracle-rdbms-server-11gR2-preinstall.x86_64 java-devel
unzip && \  
yum clean all && \  
rm -rf /var/lib/{cache,log} /var/log/lastlog && \  
mv /install/gosu-amd64 /usr/local/bin/gosu && \  
chmod +x /usr/local/bin/gosu && \  
echo "oracle:oracle" | chpasswd && \  
mkdir -p $ORACLE_BASE && chown -R oracle:oinstall $ORACLE_BASE && \  
chmod -R 775 $ORACLE_BASE && \  
mkdir -p /app/oraInventory && \  
chown -R oracle:oinstall /app/oraInventory && \  
chmod -R 775 /app/oraInventory && \  
chmod -R 775 /u01 && \  
chown -R oracle:oinstall /u01 && \  
mkdir /oracle.init.d && \  
chown -R oracle:oinstall /oracle.init.d && \  
mkdir -p /u01/app/oracle-product && chown oracle:oinstall /u01/app/oracle-
product && \  
ln -s /u01/app/oracle-product $ORACLE_BASE/product && \  
chmod +x /install/*.sh && \  
/install/download_Oracle_DB_11gR2_EE_1of2.sh && \  
/install/download_Oracle_DB_11gR2_EE_2of2.sh && \  
cd /install && unzip -qq '*.zip' && rm -f /install/*.zip && source
/install/ins_ctx.sh && source /install/ins_emagent.sh && \  
gosu oracle /install/install_sw.sh /install/sw_install.rsp && \  
rm -fr $ORACLE_SRC_INSTALL_DIR && rm -fr /tmp/*  
  
ENV INIT_MEM_PST 40  
ENV SW_ONLY false  
  
ADD entrypoint.sh /entrypoint.sh  
  
EXPOSE 1521  
EXPOSE 8080  
EXPOSE 5500  
  
VOLUME ["/u01/app/oracle"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

