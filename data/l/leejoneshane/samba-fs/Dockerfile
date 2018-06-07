FROM alpine  
  
ENV SAMBA_ADMIN_PASSWORD S@mba  
  
ADD entrypoint.sh /usr/sbin/  
ADD smb.conf /etc/samba/smb.conf  
ADD samba.schema /etc/openldap/schema/samba.schema  
ADD samba.ldif /etc/openldap/schema/samba.ldif  
ADD slapd.conf /etc/openldap/slapd.conf  
ADD initldap.ldif /etc/openldap/initldap.ldif  
ADD web /web  
  
RUN apk update \  
&& apk --no-cache --no-progress add openrc bash sudo zip acl attr samba
freeradius openldap-clients openldap \  
openldap-back-mdb perl perl-ldap perl-mojolicious \  
perl-locale-maketext-lexicon \  
&& adduser -G wheel -D -h /mnt admin \  
&& echo "wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/wheel \  
&& chmod 0440 /etc/sudoers.d/wheel \  
&& chmod +x /usr/sbin/entrypoint.sh \  
&& mkdir -p /sam/openldap \  
&& mv /etc/passwd /root/passwd \  
&& mv /etc/shadow /root/shadow \  
&& mv /etc/group /root/group \  
&& cp -p /root/passwd /sam/passwd \  
&& cp -p /root/shadow /sam/shadow \  
&& cp -p /root/group /sam/group \  
&& ln -s /sam/passwd /etc/passwd \  
&& ln -s /sam/shadow /etc/shadow \  
&& ln -s /sam/group /etc/group  
  
EXPOSE 137/udp 138/udp 139 3000  
VOLUME ["/mnt", "/sam", "/web"]  
ENTRYPOINT ["entrypoint.sh"]  

