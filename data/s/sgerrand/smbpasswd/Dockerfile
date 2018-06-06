FROM alpine  
MAINTAINER Sasha Gerrand <docker-smbpasswd@sgerrand.com>  
RUN apk add --no-cache bind-tools samba-common-tools \  
&& mkdir -p /etc/samba /var/lib/samba/private \  
&& touch /etc/samba/smb.conf \  
&& rm -fr /var/cache/apk/*  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

