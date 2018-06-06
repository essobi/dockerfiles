# 2014-11-04  
# Peter.Kutschera@ait.ac.at  
# docker build -t peterkutschera/crisma-orion .  
# docker run -P -d peterkutschera/crisma-orion  
# see https://github.com/telefonicaid/fiware-orion  
# Test:  
# docker run -t -i -P peterkutschera/orion_c /bin/bash  
# apache2ctl start  
# tail -f /var/log/apache2/error.log &  
FROM centos:centos6  
MAINTAINER Peter.Kutschera@ait.ac.at  
  
  
RUN yum install -y epel-release && \  
yum install -y make cmake gcc-c++ scons libmicrohttpd-devel boost-devel
libcurl-devel wget tar bzip2 clang CUnit-devel git crontabs && \  
yum install -y mongodb-server && \  
yum update pcre  
  
RUN chkconfig mongod on  
  
# fix problem cron not able to run root cronjobsd  
RUN perl -i.bak -p -e 's/^(session\s+required\s+pam_loginuid.so)\s*$/#\1\n/'
/etc/pam.d/crond  
  
RUN mkdir /home/src  
WORKDIR /home/src  
  
RUN wget http://downloads.mongodb.org/cxx-driver/mongodb-
linux-x86_64-2.2.3.tgz && \  
tar xfvz mongodb-linux-x86_64-2.2.3.tgz && \  
cd mongo-cxx-driver-v2.2 && scons && scons install && chmod a+r -R
/usr/local/include/mongo  
  
RUN wget http://googlemock.googlecode.com/files/gmock-1.5.0.tar.bz2 && \  
tar xfvj gmock-1.5.0.tar.bz2 && \  
cd gmock-1.5.0 && \  
./configure && \  
make && \  
make install && \  
ldconfig  
  
RUN git clone https://github.com/staropram/cantcoap && \  
cd cantcoap && \  
git checkout 749e22376664dd3adae17492090e58882d3b28a7 && \  
make && \  
cp cantcoap.h /usr/local/include && \  
cp dbg.h /usr/local/include && \  
cp nethelper.h /usr/local/include && \  
cp libcantcoap.a /usr/local/lib  
  
RUN git clone https://github.com/telefonicaid/fiware-orion && \  
cd fiware-orion && \  
git checkout 0.16.0-FIWARE-4.1.1 && \  
make && \  
make install && \  
cp etc/init.d/contextBroker.centos /etc/init.d/contextBroker && \  
chmod +x /etc/init.d/contextBroker && \  
cp etc/config/contextBroker /etc/sysconfig/ && \  
useradd -r orion && \  
mkdir /var/log/contextBroker && \  
chown orion:orion /var/log/contextBroker  
  
# RUN chkconfig --add contextBroker && chkconfig contextBroker on  
# setup logrotate  
COPY etc/logrotate.d/contextBroker /etc/logrotate.d/contextBroker  
  
# Automatic orion check && restart  
# used without apache proxy  
RUN echo '* * * * * if /usr/bin/curl -q -X GET http://localhost:1026/version |
grep -q version; then /bin/true ; else /etc/init.d/contextBroker restart; fi'
| crontab  
# This is used for orion behind apache:  
# RUN echo '* * * * * if curl --dump-header - -s -o /dev/null
http://localhost/orion/ | grep -q 503; then /etc/init.d/contextBroker restart
; fi' | crontab  
WORKDIR /root  
RUN rm -rf /home/src  
  
COPY root/bin/runAll.sh /root/bin/runAll.sh  
RUN chmod +x /root/bin/runAll.sh  
  
# Test  
# Start server  
# RUN /etc/init.d/mongod start  
# RUN contextBroker --version  
# RUN service crond start  
# RUN /etc/init.d/contextBroker  
EXPOSE 1026  
# CMD ["/usr/bin/tail", "-f", "/var/log/contextBroker/contextBroker.log"]  
CMD ["/root/bin/runAll.sh"]  

