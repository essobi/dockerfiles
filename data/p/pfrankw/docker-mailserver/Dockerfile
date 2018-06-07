FROM debian  
  
MAINTAINER Francesco Pompo'  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MASTER_PASSWORD changemeplease  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install nano patch rsyslog mysql-server postfix dovecot-core
dovecot-mysql dovecot-imapd dovecot-lmtpd  
  
RUN groupadd -g 5000 vmail  
RUN useradd -u 5000 -g vmail -s /usr/bin/nologin -d /home/vmail -m vmail  
  
RUN service mysql start && mysql -e "CREATE DATABASE postfix_db;"  
RUN service mysql start && mysql -e "GRANT ALL ON postfix_db.* TO
'postfix_user'@'localhost' IDENTIFIED BY '${MASTER_PASSWORD}';"  
RUN apt-get -y install apache2 php5 php5-imap  
RUN service mysql start && apt-get -y install postfixadmin  
  
ADD ./config.inc.php.patch /etc/postfixadmin/config.inc.php.patch  
RUN patch /etc/postfixadmin/config.inc.php
/etc/postfixadmin/config.inc.php.patch  
RUN rm /etc/postfixadmin/config.inc.php.patch  
  
RUN sed -i "s/\\\$\\\dbuser.*/\\\$\\\dbuser='postfix_user';/g"
/etc/postfixadmin/dbconfig.inc.php  
RUN sed -i "s/\\\$\\\dbpass.*/\\\$\\\dbpass='${MASTER_PASSWORD}';/g"
/etc/postfixadmin/dbconfig.inc.php  
RUN sed -i "s/\\\$\\\dbname.*/\\\$\\\dbname='postfix_db';/g"
/etc/postfixadmin/dbconfig.inc.php  
  
RUN cd /etc/ssl/private/ && openssl req -new -x509 -nodes -newkey rsa:4096
-subj "/" -keyout vmail.key -out vmail.crt -days 1460 #days are optional  
RUN cd /etc/ssl/private/ && chmod 400 vmail.key && chmod 444 vmail.crt  
  
  
ADD ./master.cf.patch /etc/postfix/master.cf.patch  
RUN patch /etc/postfix/master.cf /etc/postfix/master.cf.patch  
RUN rm /etc/postfix/master.cf.patch  
  
ADD ./main.cf.append /etc/postfix/main.cf.append  
RUN cat /etc/postfix/main.cf.append >> /etc/postfix/main.cf  
RUN rm /etc/postfix/main.cf.append  
  
RUN echo "user = postfix_user\n\  
password = ${MASTER_PASSWORD}\n\  
hosts = localhost\n\  
dbname = postfix_db\n\  
table = alias\n\  
select_field = goto\n\  
where_field = address" > /etc/postfix/virtual_alias_maps.cf  
  
RUN echo "user = postfix_user\n\  
password = ${MASTER_PASSWORD}\n\  
hosts = localhost\n\  
dbname = postfix_db\n\  
table = domain\n\  
select_field = domain\n\  
where_field = domain" > /etc/postfix/virtual_mailbox_domains.cf  
  
RUN echo "user = postfix_user\n\  
password = ${MASTER_PASSWORD}\n\  
hosts = localhost\n\  
dbname = postfix_db\n\  
table = mailbox\n\  
select_field = maildir\n\  
where_field = username" > /etc/postfix/virtual_mailbox_maps.cf  
  
RUN touch /etc/postfix/transport  
RUN postmap /etc/postfix/transport  
  
RUN mv /etc/dovecot/dovecot.conf /etc/dovecot/dovecot.conf.orig  
ADD ./dovecot.conf /etc/dovecot/dovecot.conf  
  
RUN echo "driver = mysql\n\  
connect = host=localhost dbname=postfix_db user=postfix_user
password=${MASTER_PASSWORD}\n\  
default_pass_scheme = SHA512\n\  
user_query = SELECT '/home/vmail/%d/%n' as home, 'maildir:/home/vmail/%d/%n'
as mail, 5000 AS uid, 5000 AS gid, concat('dirsize:storage=', quota) AS quota
FROM mailbox WHERE username = '%u' AND active = '1'\n\  
password_query = SELECT username as user, password, '/home/vmail/%d/%n' as
userdb_home, 'maildir:/home/vmail/%d/%n' as userdb_mail, 5000 as userdb_uid,
5000 as userdb_gid FROM mailbox WHERE username = '%u' AND active = '1'" >
/etc/dovecot/dovecot-sql.conf  
  
  
ADD ./10-master.conf.patch /etc/dovecot/conf.d/10-master.conf.patch  
RUN patch /etc/dovecot/conf.d/10-master.conf
/etc/dovecot/conf.d/10-master.conf.patch  
RUN rm /etc/dovecot/conf.d/10-master.conf.patch  
  
RUN echo "export TERM=xterm" >> /root/.bashrc  
  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 25 587 993  
  
VOLUME ["/var/log", "/var/lib/mysql", "/etc/postfixadmin", "/home/vmail"]  
  
CMD ["/bin/bash", "/start.sh"]  

