FROM ubuntu  
MAINTAINER Stefan Baur  
  
COPY overlay/ /  
  
RUN chmod +x /scripts/*; sleep 1; /scripts/setup; /scripts/cleanup -f bash df
awk mawk seq wc diff patch cut chmod xargs tr sh egrep tempfile locale id dash
cat tail head logger echo sed test dirname basename uname start-stop-daemon
getopt hostname java touch read ps kill cp patch find tty which mktemp rm mv
mkdir ln chown grep groups ls du git git-receive-pack git-shell git-upload-
archive git-upload-pack sudo bundle node nodejs npm grunt nc nc.traditional
nc.openbsd sleep env mysql mysqld mysql_client_test mysql_convert_table_format
mysql_find_rows mysql_fix_extensions mysql_install_db mysql_plugin
mysql_secure_installation mysql_setpermission mysql_tzinfo_to_sql
mysql_upgrade mysql_waitpid mysql_zap mysqlaccess mysqladmin mysqlanalyze
mysqlbinlog mysqlbug mysqlcheck mysqld_multi mysqld_safe mysqldump
mysqldumpslow mysqlhotcopy mysqlimport mysqloptimize mysqlrepair mysqlreport
mysqlshow mysqlslap mysqltest apache2 apache2ctl apachectl perl perl5.18.2
perlbug perldoc perlivp perlthanks hunspell install su  
  
WORKDIR /data  
  
CMD /ox.sh  
  
EXPOSE 80  

