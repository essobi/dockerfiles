FROM alpine:latest  
  
MAINTAINER Troy Kelly <troy.kelly@really.ai>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Docker image to provide the net-snmp daemon" \  
org.label-schema.description="Provides snmpd for CoreOS and other small
footprint environments without package managers" \  
org.label-schema.url="https://really.ai/about/opensource" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/reallyreally/docker-snmpd" \  
org.label-schema.vendor="Really Really, Inc." \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
EXPOSE 161 161/udp  
  
RUN apk add --update \--no-cache linux-headers alpine-sdk curl findutils sed
python2 && \  
mkdir -p /etc/snmp && \  
curl -L "https://sourceforge.net/projects/net-snmp/files/5.4.5-pre-
releases/net-snmp-5.4.5.rc1.tar.gz/download" -o net-snmp.tgz && \  
curl -L "https://raw.githubusercontent.com/librenms/librenms-
agent/master/snmp/nginx-stats" -o /etc/snmp/nginx-stats && \  
curl -L "https://raw.githubusercontent.com/librenms/librenms-
agent/master/snmp/distro" -o /usr/bin/distro && \  
sed -i "s!http://127.0.0.1/nginx-status!http://nginx/nginx-status!g"
/etc/snmp/nginx-stats && \  
sed -i "s/^#!\/usr\/bin\/env bash/#!\/usr\/bin\/env sh/g" /usr/bin/distro && \  
chmod +x /etc/snmp/nginx-stats && \  
chmod +x /usr/bin/distro && \  
tar zxvf net-snmp.tgz && \  
cd net-snmp-* && \  
find . -type f -print0 | xargs -0 sed -i 's/\"\/proc/\"\/host_proc/g' && \  
./configure --prefix=/usr/local \--disable-ipv6 --disable-snmpv1 --with-
defaults && \  
make -j$(nproc) && \  
make install && \  
cd .. && \  
rm -Rf ./net-snmp* && \  
apk del linux-headers alpine-sdk curl findutils sed  
  
COPY snmpd.conf /etc/snmp  
  
CMD [ "/usr/local/sbin/snmpd", "-f", "-c", "/etc/snmp/snmpd.conf" ]  

