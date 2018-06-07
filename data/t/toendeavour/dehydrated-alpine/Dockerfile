FROM alpine:latest  
LABEL maintainer="Marc Mettke <marc@itmettke.de>"  
  
ENV VERSION="v0.6.2"  
ENV
DEHYDRATED_URL="https://raw.githubusercontent.com/lukas2511/dehydrated/${VERSION}/dehydrated"  
ENV CLOUDFLARE_HOOK_URL="https://github.com/kappataumu/letsencrypt-cloudflare-
hook"  
ENV DEPENDENCIES="bash openssl curl python py-cffi py-cryptography py-
dnspython py-enum34 py-future py-idna py-ipaddress py-ndg_httpsclient py2-asn1
py2-cparser py-openssl py-requests py-six py-pip"  
ENV BUILD_DEPENDENCIES="gcc py-pip python2-dev linux-headers musl-dev libffi-
dev openssl-dev"  
  
COPY crontab /var/spool/cron/crontabs/cert-renew  
COPY config /etc/dehydrated/config  
  
RUN apk --no-cache add ${DEPENDENCIES} && \  
pip install tld wheel  
RUN apk --no-cache add git && \  
wget ${DEHYDRATED_URL} \  
\--directory-prefix /usr/local/bin/ && \  
chmod +x /usr/local/bin/dehydrated && \  
git clone ${CLOUDFLARE_HOOK_URL} /etc/dehydrated/hooks/cloudflare && \  
apk del git  
  
VOLUME /etc/dehydrated/data  
  
CMD /usr/sbin/crond -fd15  
HEALTHCHECK CMD /bin/ash -c "PID=\$(cat /var/run/crond.pid) && [ -n
\"\${PID}\" -a -d \"/proc/\${PID}\" ] && exit 0 || exit 1"  

