FROM centos:7  
MAINTAINER "Zebula Sampedro" <sampedro@colorado.edu>  
  
RUN yum install -y epel-release \  
&& yum update -y \  
&& yum install -y 389-ds-base 389-adminutil \  
&& yum clean all  
  
ADD ds-setup.inf /tmp/ds-setup.inf  
ADD ldapconf.ldif /tmp/ldapconf.ldif  
# The 389-ds setup will fail because the hostname can't be reliably
determined, so we'll bypass it and then install.  
RUN useradd ldapadmin \  
&& rm -fr /var/lock /usr/lib/systemd/system \  
&& sed -i 's/checkHostname {/checkHostname {\nreturn();/g'
/usr/lib64/dirsrv/perl/DSUtil.pm \  
&& sed -i 's/updateSelinuxPolicy($inf);//g' /usr/lib64/dirsrv/perl/* \  
&& sed -i '/if (@errs = startServer($inf))/,/}/d' /usr/lib64/dirsrv/perl/* \  
&& setup-ds.pl \--silent \--file /tmp/ds-setup.inf \  
&& /usr/sbin/ns-slapd -D /etc/dirsrv/slapd-dir \  
&& sleep 3 \  
&& ldapadd -H ldap:/// -f /tmp/ldapconf.ldif -x -D "cn=Directory Manager" -w
password  
  
EXPOSE 389  
  
CMD /usr/sbin/ns-slapd -D /etc/dirsrv/slapd-dir && tail -F
/var/log/dirsrv/slapd-dir/access  

