FROM debian:latest  
  
# Enable non-free  
RUN sed -i -e 's/$/ contrib non-free/g' /etc/apt/sources.list && \  
sed -i -e 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g'
/etc/apt/sources.list && \  
sed -i -e 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g'
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y libsnmp-dev snmp-mibs-downloader
snmptrapd  
  
RUN rm -rf /etc/mysql  
  
ENV MY_CNF /etc/my.cnf  
ENV SNMPTRAPD_COMMUNITY public  
ENV SNMPTRAPD_DB_USER user  
ENV SNMPTRAPD_DB_PASS secret  
ENV SNMPTRAPD_DB_HOST localhost  
ENV SNMPTRAPD_SQL_MAX_QUEUE 140  
ENV SNMPTRAPD_SQL_SAVE_INTERVAL 9  
RUN echo "sqlMaxQueue $SNMPTRAPD_SQL_MAX_QUEUE" >> /etc/snmp/snmptrapd.conf &&
\  
echo "sqlSaveInterval $SNMPTRAPD_SQL_SAVE_INTERVAL" >>
/etc/snmp/snmptrapd.conf  
  
CMD echo "authCommunity log $SNMPTRAPD_COMMUNITY" >> /etc/snmp/snmptrapd.conf
&& \  
echo "[snmptrapd]" >> $MY_CNF && \  
echo "user=$SNMPTRAPD_DB_USER" >> $MY_CNF && \  
echo "password=$SNMPTRAPD_DB_PASS" >> $MY_CNF && \  
echo "host=$SNMPTRAPD_DB_HOST" >> $MY_CNF && \  
echo "dummy=" >> $MY_CNF && \  
snmptrapd -Lo -f udp6:162  

