FROM centos:centos7  
MAINTAINER Tomohisa Hirami<hirami@io-architect.com>  
  
# create users, set locales  
RUN useradd -m helpdesk && \  
useradd -m cust01 && useradd -m cust02 && useradd -m cust03 && useradd -m
cust04 && useradd -m cust05 && \  
useradd -m agent01 && useradd -m agent02 && useradd -m agent03 && useradd -m
agent04 && useradd -m agent05 && \  
cp /usr/share/zoneinfo/Japan /etc/localtime && \  
localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \  
echo helpdesk | passwd --stdin helpdesk && echo cust01 | passwd --stdin cust01
&& echo cust02 | passwd --stdin cust02 && \  
echo cust03 | passwd --stdin cust03 && echo cust04 | passwd --stdin cust04 &&
echo cust05 | passwd --stdin cust05 && \  
echo agent01 | passwd --stdin agent01 && echo agent02 | passwd --stdin agent02
&& echo agent03 | passwd --stdin agent03 && \  
echo agent04 | passwd --stdin agent04 && echo agent05 | passwd --stdin agent05  
  
RUN yum install -y httpd rsyslog cronie crontabs cronie-anacron epel-release
postfix dovecot  
  
# install from epel  
RUN yum install -y supervisor squirrelmail  
  
# Copy Supervisord, Postfix, Dovecot confs  
COPY etc /etc/  
  
# Squirrelmail  
RUN chown root.apache /etc/squirrelmail/config.php  
  
# Squirrelmail日本語対応  
# http://taka2.info/20120705/squirrelmail-php54/  
#  
RUN find /usr/share/squirrelmail -name '*.php' -print \  
| xargs egrep -l 'htmlspecialchars *\\([^\\)]' \  
| egrep -v 'global.php|configtest.php|login.php|class/|contrib/' \  
| xargs perl -i.bak -pe 's/htmlspecialchars *\\([^\\)]/sq_$&/'  
COPY ext_i18n.php /  
RUN cat /ext_i18n.php >> /usr/share/squirrelmail/functions/i18n.php  
  
# MySQL  
COPY mysql57-community-release-el7-8.noarch.rpm /  
RUN yum install -y mysql57-community-release-el7-8.noarch.rpm && yum install
-y mysql-community-server && \  
rm mysql57-community-release-el7-8.noarch.rpm  
  
COPY mysql_init.sh /  
RUN chmod 755 mysql_init.sh ; sync ; /mysql_init.sh  
  
# OTRS  
# perl modules  
RUN yum install -y "perl(Crypt::Eksblowfish::Bcrypt)" && \  
yum install -y "perl(DBD::mysql)" && \  
yum install -y "perl(JSON::XS)" && \  
yum install -y "perl(Mail::IMAPClient)" && \  
yum install -y "perl(ModPerl::Util)" && \  
yum install -y "perl(Text::CSV_XS)" && \  
yum install -y "perl(YAML::XS)"  
  
# RPMインストール  
ENV OTRS_RPM=otrs-5.0.23-01.noarch.rpm  
RUN curl -o /$OTRS_RPM http://ftp.otrs.org/pub/otrs/RPMS/rhel/7/$OTRS_RPM && \  
yum install -y $OTRS_RPM && \  
rm /$OTRS_RPM  
  
# 設定ファイル類  
COPY opt /opt/  
RUN /opt/otrs/bin/otrs.SetPermissions.pl --web-group=apache  
  
# 起動スクリプト  
COPY otrs.sh /  
RUN chmod 755 /otrs.sh  
  
EXPOSE 80  
CMD ["/otrs.sh"]  

