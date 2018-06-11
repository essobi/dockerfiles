FROM centos:7  
#install oracle client  
COPY ./oracle /tmp/oracle  
RUN yum install -y /tmp/oracle/oracle-
instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm\  
/tmp/oracle/oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm\  
/tmp/oracle/oracle-instantclient12.2-tools-12.2.0.1.0-1.x86_64.rpm\  
&& sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-
instantclient.conf" && ldconfig\  
&& rm -rf /tmp/oracle  
ENV PATH /usr/lib/oracle/12.2/client64/bin:$PATH  

