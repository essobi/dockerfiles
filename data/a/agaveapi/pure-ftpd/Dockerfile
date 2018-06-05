######################################################  
#  
# Agave FTP storage Server  
# Tag: agaveapi/pure-ftpd  
#  
# This is the base FTP server image used for testing  
# FTP in the Agave API. It extends from the agaveapi/centos-base  
# image with a pure-ftp server which defaults to the  
# system accounts and user home directories. Anonymous access  
# is also supported.  
#  
# https://bitbucket.org/taccaci/agave-environment  
#  
######################################################  
  
FROM agaveapi/centos-base  
  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu>  
  
RUN yum install -y tar rsyslog gzip wget gcc pam-devel && \  
cd /tmp && \  
wget http://download.pureftpd.org/pub/pure-ftpd/releases/pure-
ftpd-1.0.40.tar.gz && \  
tar -xvzf pure-ftpd-1.0.40.tar.gz && \  
cd pure-ftpd-1.0.40 && \  
CPPFLAGS='-DANON_CAN_DELETE=1 -DANON_CAN_RENAME=1 -DANON_CAN_RESUME=1
-DANON_CAN_CHANGE_PERMS=1' ./configure --without-capabilities --with-
virtualchroot --with-pam --with-altlog --with-wrapper --with-cookie --with-
throttling --with-ratios --with-paranoidmsg --with-quotas && \  
make && \  
make install && \  
yum erase -y wget tar pam-devel gcc pam-devel && \  
echo "ftp.* /var/log/ftpd" >> /etc/rsyslog.conf && \  
mkdir /var/ftp && \  
chown -R ftp:ftp /var/ftp  
  
VOLUME /home/testuser /home/testotheruser /home/testshareuser  
ADD supervisord.conf /etc/supervisord.conf  
EXPOSE 20 21 30000 30001 30002 30003 30004 30005 30006 30007 30008 30009 30010
30011 30012 30013 30014 30015 30016 30017 30018 30019 30020 30021 30022 30023
30024 30025 30026 30027 30028 30029 30030 30031 30032 30033 30034 30035 30036
30037 30038 30039 30040 30041 30042 30043 30044 30045 30046 30047 30048 30049
30050 30051 30052 30053 30054 30055 30056 30057 30058 30059 30060 30061 30062
30063 30064 30065 30066 30067 30068 30069 30070 30071 30072 30073 30074 30075
30076 30077 30078 30079 30080 30081 30082 30083 30084 30085 30086 30087 30088
30089 30090 30091 30092 30093 30094 30095 30096 30097 30098 30099  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

