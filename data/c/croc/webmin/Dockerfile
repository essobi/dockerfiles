FROM centos  
  
#ENV ROOT_PASS SuperSecret  
ARG ROOT_PASS=SuperSecret  
  
# install basic packages and webmin requirements for LDAP management  
RUN yum install -y net-tools perl perl-Net-SSLeay openssl perl-LDAP perl-XML-
Parser perl-Encode-Detect openssh-clients  
# download webmin  
RUN curl -L -o /opt/webmin.rpm
https://prdownloads.sourceforge.net/webadmin/webmin-1.881-1.noarch.rpm && rpm
-i /opt/webmin.rpm  
  
# create a user for webmin  
#RUN useradd -g users -m -s /bin/bash webmin && echo MySecret | passwd webmin
--stdin  
# set root password for webmin  
RUN echo $ROOT_PASS | passwd root --stdin  
  
COPY files/* /opt/  
RUN chmod 755 /opt/*sh  
  
ENTRYPOINT /opt/start.sh  
  

