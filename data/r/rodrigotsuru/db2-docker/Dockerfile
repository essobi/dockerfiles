FROM centos:6.6  
MAINTAINER Rodrigo Tsuru <caixapostal@gmail.com>  
# Install required libs  
#
http://www-01.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.qb.server.doc/doc/r0008865.html?cp=SSEPGG_10.5.0%2F2-0-1-2-2-4&lang=en  
RUN yum install -y libaio.i686 \  
libaio.x86_64 \  
pam.i686 \  
pam.x86_64 \  
libstdc++.i686 \  
libstdc++.x86_64 \  
compat-libstdc++-33.i686 \  
compat-libstdc++-33.x86_64 \  
glibc.i686 \  
glibc.x86_64 \  
libgcc.i686 \  
libgcc.x86_64 \  
sg3_utils \  
kernel-devel \  
gcc-c++ \  
wget \  
tar \  
file \  
ksh.x86_64 \  
patch \  
ntpd \  
gcc  
  
# Copies the script to downalod  
RUN cd /tmp && wget
https://googledrive.com/host/0B1TfHhOuw5TLMWw2YkNITVhWWjQ/v10.5_linuxx64_server_t.tar.gz  
RUN cd /tmp && \  
tar -zvxf v10.5_linuxx64_server_t.tar.gz && \  
rm v10.5_linuxx64_server_t.tar.gz  
# Copies the response file  
COPY db2server.rsp /tmp/db2server.rsp  
# Install DB2 and remove the installer.  
RUN cd /tmp/server_t && \  
./db2prereqcheck -v 10.5.0.5 && \  
( ./db2setup -r /tmp/db2server.rsp && \  
cat /tmp/db2setup.log || cat /tmp/db2setup.log ) && \  
/opt/ibm/db2/V10.5/bin/db2val -o && \  
cd && \  
rm -Rf /tmp/server_t && \  
rm /tmp/db2server.rsp  

