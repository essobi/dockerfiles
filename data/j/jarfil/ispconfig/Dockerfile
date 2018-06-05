#  
# Dockerfile for ISPConfig with MariaDB database  
#  
# https://www.howtoforge.com/tutorial/perfect-server-debian-8-jessie-apache-
bind-dovecot-ispconfig-3/  
#  
FROM debian:jessie  
  
MAINTAINER Jaroslaw Filiochowski <jarfil@gmail.com>  
  
# --- 5 Update Your Debian Installation  
ADD ./etc/apt/sources.list /etc/apt/sources.list  
# --- 8 Install Postfix, Dovecot, MySQL, phpMyAdmin, rkhunter, binutils  
ADD ./etc/postfix/master.cf /etc/postfix/master.cf  
# --- 9 Install Amavisd-new, SpamAssassin And Clamav  
ADD ./etc/clamav/clamd.conf /etc/clamav/clamd.conf  
# --- 10 Install Apache2, PHP5, phpMyAdmin, FCGI, suExec, Pear, And mcrypt  
# --- 12 XCache and PHP-FPM  
# --- 13 Install Mailman  
ADD ./etc/aliases /etc/aliases  
# --- 14 Install PureFTPd And Quota  
ADD ./etc/default/pure-ftpd-common /etc/default/pure-ftpd-common  
# --- 15 Install BIND DNS Server  
# --- 16 Install Vlogger, Webalizer, And AWStats  
ADD etc/cron.d/awstats /etc/cron.d/  
# --- 17 Install Jailkit  
# --- 18 Install fail2ban  
ADD ./etc/fail2ban/jail.local /etc/fail2ban/jail.local  
ADD ./etc/fail2ban/filter.d/pureftpd.conf /etc/fail2ban/filter.d/pureftpd.conf  
ADD ./etc/fail2ban/filter.d/dovecot-pop3imap.conf
/etc/fail2ban/filter.d/dovecot-pop3imap.conf  
# --- 19 Install squirrelmail  
ADD ./etc/apache2/conf-enabled/squirrelmail.conf /etc/apache2/conf-
enabled/squirrelmail.conf  
ADD ./etc/squirrelmail/config.php /etc/squirrelmail/config.php  
# --- 20 Install ISPConfig 3  
# ADD ./etc/mysql/my.cnf /etc/mysql/my.cnf  
ADD ./etc/postfix/master.cf /etc/postfix/master.cf  
ADD ./etc/clamav/clamd.conf /etc/clamav/clamd.conf  
  
EXPOSE 20 21 22 53/udp 53/tcp 80 443 953 8080 30000 30001 30002 30003 30004
30005 30006 30007 30008 30009 3306  
# ISPCONFIG Initialization and Startup Script  
ADD ./start.sh /start.sh  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
ADD ./etc/cron.daily/sql_backup.sh /etc/cron.daily/sql_backup.sh  
ADD ./autoinstall.ini /tmp/ispconfig3_install/install/autoinstall.ini  
ADD ./bin/systemctl /bin/systemctl  
  
ADD ./ISPConfig_Clean-3.0.5 /tmp/ISPConfig_Clean-3.0.5  
  
# bunched-up run  
ADD ./make.sh /make.sh  
RUN chmod 755 /make.sh  
RUN ["/bin/bash", "-c", "/make.sh"]  
  
VOLUME
["/var/www/","/var/mail/","/var/backup/","/var/lib/mysql","/etc/","/usr/local/ispconfig","/var/log/"]  
  
CMD ["/bin/bash", "/start.sh"]  

