FROM alpine:latest  
  
MAINTAINER AusNimbus <support@ausnimbus.com.au>  
  
LABEL io.k8s.description="New Relic Linux Server Monitor" \  
io.k8s.display-name="nrsysmond"  
  
ENV NRSYSMOND_VERSION 2.3.0.132  
ENV GLIBC_VERSION 2.23-r3  
  
ADD https://download.newrelic.com/server_monitor/release/newrelic-
sysmond-${NRSYSMOND_VERSION}-linux.tar.gz /newrelic-sysmond.tar.gz  
ADD https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk
/glibc-${GLIBC_VERSION}.apk  
  
RUN apk add --allow-untrusted glibc-${GLIBC_VERSION}.apk && \  
tar xvfz /newrelic-sysmond.tar.gz && \  
rm /newrelic-sysmond.tar.gz && \  
mkdir /etc/newrelic && \  
mv /newrelic-sysmond-${NRSYSMOND_VERSION}-linux/daemon/nrsysmond.x64
/usr/sbin/nrsysmond && \  
mv /newrelic-sysmond-${NRSYSMOND_VERSION}-linux/scripts/nrsysmond-config
/usr/sbin/nrsysmond-config && \  
mv /newrelic-sysmond-${NRSYSMOND_VERSION}-linux/nrsysmond.cfg /etc/newrelic/
&& \  
#sed -i 's/^#host_root=\/host/host_root=\/host/g' /etc/newrelic/nrsysmond.cfg
&& \  
rm -rf newrelic-sysmond-*-linux*  
  
COPY bin/container-entrypoint /usr/sbin/  
  
ENTRYPOINT ["container-entrypoint"]  
CMD ["/usr/sbin/nrsysmond", "-E", "-F", "-l", "/dev/stdout"]  

