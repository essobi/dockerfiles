# Bamboo Agent  
FROM openjdk:alpine  
MAINTAINER Jim Davies  
  
ENV AGENT_VERSION=6.1.1  
ENV BAMBOO_SERVER_HOST=my-bamboo-server  
ENV BAMBOO_SERVER_PORT=8085  
ENV GLIBC_VERSION=2.23-r1  
ENV LANG=C.UTF-8  
COPY bamboo-agent.sh /bamboo-agent.sh  
  
RUN \  
apk add --update \  
ca-certificates \  
git \  
openssh \  
wget \  
&& wget -O /tmp/glibc.apk "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \  
&& apk add --allow-untrusted /tmp/glibc.apk \  
&& wget -O /tmp/glibc-bin.apk "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" \  
&& apk add --allow-untrusted /tmp/glibc-bin.apk \  
&& /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/* \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
CMD ["/bamboo-agent.sh"]  

