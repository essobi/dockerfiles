FROM alpine  
MAINTAINER Steve Coffman  
  
RUN apk add --update bash && \  
apk add --no-cache util-linux && \  
apk add --no-cache bind-tools samba-common-tools && \  
mkdir -p /etc/samba /var/lib/samba/private && \  
touch /etc/samba/smb.conf && \  
rm -fr /var/cache/apk/*  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["/bin/bash", "-c", "/usr/local/bin/docker-entrypoint.sh ${*}",
"--"]  

