FROM alpine  
  
ENV DNSMASQ_REGEX_VERSION 2.78-r1  
ENV PAMTESTER_VERSION 0.1.2  
RUN apk add --update --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" > /etc/timezone && apk del tzdata  
RUN apk add --update curl bash su-exec && curl -fsSL
https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz | tar xzv
-C /usr/local/bin && chmod +x /usr/local/bin/forego  
  
RUN curl -LOsS https://github.com/cuckoohello/dnsmasq-
regex/raw/alpine/dnsmasq-regex-${DNSMASQ_REGEX_VERSION}.apk && \  
apk add --update --no-cache --allow-untrusted dnsmasq-
regex-${DNSMASQ_REGEX_VERSION}.apk && \  
rm dnsmasq-regex-${DNSMASQ_REGEX_VERSION}.apk  
  
RUN apk add --update --no-cache openvpn openvpn-auth-pam nss-pam-ldapd ipset
iptables && printf "auth sufficient pam_ldap.so\naccount sufficient
pam_permit.so" > /etc/pam.d/openvpn  
  
RUN apk add --update --no-cache --virtual .build-deps build-base linux-pam-dev
&& curl -LsS -o /tmp/pamtester-${PAMTESTER_VERSION}.tar.gz
https://managedway.dl.sourceforge.net/project/pamtester/pamtester/${PAMTESTER_VERSION}/pamtester-${PAMTESTER_VERSION}.tar.gz
&& tar xf /tmp/pamtester-${PAMTESTER_VERSION}.tar.gz -C /tmp && cd
/tmp/pamtester-${PAMTESTER_VERSION} && ./configure --prefix=/usr && make &&
strip ./src/pamtester && cp src/pamtester /usr/bin && rm -rf
/tmp/pamtester-${PAMTESTER_VERSION} /tmp/pamtester-${PAMTESTER_VERSION}.tar.gz
&& apk del .build-deps  
  
ADD Procfile docker-compose.yml docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["forego", "start", "-r"]  

