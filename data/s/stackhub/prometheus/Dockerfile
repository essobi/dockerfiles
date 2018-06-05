# Because the idea is to build Stackhub containers from common bases we _and_  
# Docker does not support composition we will inherit from stackhub/base-confd  
# then shoehorn in glibc  
FROM stackhub/base-confd  
MAINTAINER Boyd Hemphill <boyd@stackengine.com>  
  
#  
# Upgrade OS and shoehorn in glibc  
# thanks to sdurrheimer/alpine-glibc and  
# Andy Shinn - https://github.com/gliderlabs/docker-alpine/issues/11  
#  
ENV \  
ALPINE_GLIBC_URL="https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/" \  
GLIBC_PKG="glibc-2.21-r2.apk" \  
GLIBC_BIN_PKG="glibc-bin-2.21-r2.apk"  
  
RUN \  
apk add --update -t deps wget ca-certificates openssl \  
&& apk add --update -t openssl \  
&& cd /tmp \  
&& wget ${ALPINE_GLIBC_URL}${GLIBC_PKG} ${ALPINE_GLIBC_URL}${GLIBC_BIN_PKG} \  
&& apk add --allow-untrusted ${GLIBC_PKG} ${GLIBC_BIN_PKG} \  
&& /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf \  
&& apk del --purge deps \  
&& rm /tmp/* /var/cache/apk/*  
  
#  
# Prometheus is not a package for Alpine so running with scissors.  
#  
# Set the version of prometheus  
ENV PROM_VER="0.16.0"  
ENV GH_URL="https://github.com/prometheus/prometheus/releases/download"  
# Get prometheus from github releases  
  
RUN \  
wget \  
-O /tmp/prometheus.tar.gz \  
${GH_URL}/${PROM_VER}/prometheus-${PROM_VER}.linux-amd64.tar.gz && \  
tar -xzf /tmp/prometheus.tar.gz -C /tmp && \  
mkdir -p /etc/prometheus && \  
mv /tmp/prometheus-${PROM_VER}.linux-amd64/prometheus /bin/ && \  
mv /tmp/prometheus-${PROM_VER}.linux-amd64/promtool /bin/ && \  
mv /tmp/prometheus-${PROM_VER}.linux-amd64/console_libraries/ \  
/etc/prometheus/ && \  
mv /tmp/prometheus-${PROM_VER}.linux-amd64/consoles/ \  
/etc/prometheus/ && \  
rm -rfv /tmp/prometheus*  
  
#  
# Now lay down all the templating  
#  
# Basic config so prometheus starts even if there is a problem with confd  
ADD \  
prometheus/prometheus.yml.stub \  
/etc/prometheus/prometheus.yml  
  
ADD \  
prometheus/prometheus.yml.template_orig \  
/etc/confd/templates/prometheus.yml.template_orig  
  
ADD \  
prometheus/prometheus.toml.template \  
/etc/confd/conf.d/prometheus.toml.template  
  
RUN \  
mkdir -pv /etc/sv/prometheus && \  
chmod 2775 /etc/sv/prometheus && \  
ln -sv /etc/sv/prometheus /service  
  
ADD \  
prometheus/prometheus.sh \  
/etc/sv/prometheus/run  
  
ENTRYPOINT ["/sbin/runsvdir", "/service"]

