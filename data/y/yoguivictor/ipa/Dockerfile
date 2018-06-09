FROM centos:6  
MAINTAINER yoguivictor @ gmail.com  
  
RUN yum -y install --setopt=tsflags=nodocs \  
ipa-server bind bind-dyndb-ldap perl \  
&& rm -rf /lib/modules \  
/usr/share/{man,doc,info,cracklib} \  
/sbin/sln \  
/boot \  
&& yum clean all  
  
RUN sed -i 's/daemon --check/daemon --user "dbus -g root" --check/' \  
/etc/init.d/messagebus  
  
ADD bin/ /usr/local/bin/  
  
CMD ["ipa-start"]  
  

