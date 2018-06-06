FROM alpine:latest  
  
COPY ./scripts/* /root/  
  
RUN \  
echo " ---> Updating APK" && \  
apk update && \  
echo " ---> Install MariaDB" && \  
apk add mariadb && \  
echo " ---> Setting file permissions" && \  
chmod +x /root/run.sh && \  
echo " ---> Removing 'redundant' MySQL binaries" && \  
# Uncomment binaries to keep and rebuild as needed  
for file in \  
aria_chk \  
aria_dump_log \  
aria_ftdump \  
aria_pack \  
aria_read_log \  
innochecksum \  
mariabackup \  
mbstream \  
msql2mysql \  
# my_print_defaults \  
myisamchk \  
myisamlog \  
myisampack \  
# mysql \  
mysql_client_test_embedded \  
mysql_convert_table_format \  
mysql_embedded \  
# mysql_install_db \  
mysql_plugin \  
mysql_secure_installation \  
mysql_setpermission \  
mysql_tzinfo_to_sql \  
mysql_upgrade \  
mysql_zap \  
# mysqladmin \  
mysqlbinlog \  
# mysqld \  
mysqld_multi \  
mysqld_safe \  
mysqld_safe_helper \  
mysqlhotcopy \  
mysqlslap \  
mysqltest \  
mysqltest_embedded \  
mytop \  
perror \  
replace \  
resolve_stack_dump \  
# resolveip \  
wsrep_sst_common \  
wsrep_sst_mariabackup \  
wsrep_sst_mysqldump \  
wsrep_sst_rsync \  
wsrep_sst_xtrabackup \  
wsrep_sst_xtrabackup-v2 \  
;do rm /usr/bin/${file}; done && \  
echo " ---> Removing MySQL language files" && \  
# Removing language files, uncomment to keep and rebuild as needed  
for file in \  
czech \  
danish \  
dutch \  
# english \  
estonian \  
french \  
german \  
greek \  
hungarian \  
italian \  
japanese \  
korean \  
norwegian \  
norwegian-ny \  
polish \  
portuguese \  
romanian \  
russian \  
serbian \  
slovak \  
spanish \  
swedish \  
ukrainian \  
;do rm -rf /usr/share/mysql/${file}; done && \  
echo " ---> Cleaning up" && \  
rm -f /var/cache/apk/*  
  
VOLUME ["/var/lib/mysql"]  
EXPOSE 3306  
ENTRYPOINT [ "/root/run.sh" ]  

