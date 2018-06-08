FROM pataquets/apache:trusty  
  
RUN \  
apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
31C8EDC0 && \  
echo "deb http://ppa.launchpad.net/linotp/stable/ubuntu trusty main" \  
| tee -a /etc/apt/sources.list.d/linotp.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
linotp \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
# Disable Apache logging to file and use parent's image logging to stderr
configuration.  
RUN \  
sed -i 's/ErrorLog/#ErrorLog/g' /etc/apache2/sites-available/linotp2.conf && \  
nl /etc/apache2/sites-available/linotp2.conf  
  
# Replace all LinOTP logging to /var/log/linotp/linotp.log for stdout  
RUN \  
sed -i 's/\/var\/log\/linotp\/linotp.log/stdout/g' /etc/linotp2/linotp.ini &&
\  
nl /etc/linotp2/linotp.ini  
  
# Replace 'localhost' by 'smtp' as SMTP server.  
RUN \  
sed -i 's/smtpserver = localhost/smtpserver = smtp/g' /etc/linotp2/linotp.ini
&& \  
nl /etc/linotp2/linotp.ini  
  
# Comment out MySQL provided url and provide SQLite as default  
RUN \  
sed -i 's/^sqlalchemy.url =/sqlalchemy.url =
sqlite:\/\/\/\/tmp\/token.sqlite\n#sqlalchemy.url =/g' /etc/linotp2/linotp.ini
&& \  
nl /etc/linotp2/linotp.ini && \  
paster setup-app /etc/linotp2/linotp.ini && \  
chmod -v a+rw /tmp/token.sqlite  
  
ADD
https://raw.githubusercontent.com/LinOTP/LinOTP/master/linotpd/src/tools/linotp-
create-htdigest /usr/local/bin/  
RUN chmod -v a+rx /usr/local/bin/linotp-create-htdigest  
RUN linotp-create-htdigest admin admin  

