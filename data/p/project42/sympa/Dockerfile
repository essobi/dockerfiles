FROM project42/syslog-centos:centos7  
MAINTAINER Rance Hall rance_hall@icloud.com  
  
ENV SYMPA_DOMAIN=lists.mydomain.com  
ENV SYMPA_DB_TYPE=mysql  
ENV SYMPA_DB_HOST=localhost  
ENV SYMPA_DB_USER=sympa  
ENV SYMPA_DB_PASS=sympa  
ENV SYMPA_DB_NAME=sympa  
ENV SYMPA_LISTMASTERS=myadmin@mydomain.com  
ENV SYMPA_POSTFIX_RELAY=mail.mydomain.com  
ENV SYMPA_RUN_SPECIAL=FALSE  
ENV SYMPA_RUN_URL=NONE  
ENV SYMPA_RUN_NAME=NONE  
  
COPY container-files /  
  
RUN yum -y update \  
&& yum -y install wget \  
&& yum -y install epel-release \  
&& yum -y install sympa sympa-nginx \  
&& yum -y install rsync \  
&& yum -y install postfix \  
&& rpm -e --nodeps ssmtp \  
&& yum -y clean all  
  
#RUN ln -s /usr/bin/perl /bin/perl  
#The above line fixes a perl install bug that occasionally misses creating  
# a required symlink  
RUN chmod +x /usr/sbin/presympa  
  
# address data persistence needs for files in:  
#/etc/sympa  
#/var/lib/sympa  
#/var/spool/postfix  
#/var/spool/sympa #/var/spool/sympa not created by rpm package.  
RUN mkdir -p /keep/sympaetc \  
&& mkdir -p /keep/sympalib \  
&& mkdir -p /keep/postfixspool \  
&& mkdir -p /sympa_perm/sympaspool \  
&& rsync -a -r /etc/sympa/ /keep/sympaetc/ \  
&& rsync -a -r /var/lib/sympa/ /keep/sympalib/ \  
&& rsync -a -r /var/spool/postfix/ /keep/postfixspool/  
  
RUN mv /keep/sympalib/sympa_aliases /keep/sympalib/sympa_aliases.default \  
&& mv /keep/sympalib/transport_regexp /keep/sympalib/transport_regexp.default  
  
ENTRYPOINT ["/init"]  

