FROM codeworksio/ubuntu:18.04-20180210  
# SEE: https://github.com/docker-library/openjdk/blob/master/8-jdk/Dockerfile  
ARG APT_PROXY  
ARG APT_PROXY_SSL  
ENV JAVA_VERSION="8u151" \  
JAVA_UBUNTU_VERSION="8u151-b12-1" \  
CA_CERTIFICATES_JAVA_VERSION="20170930" \  
JAVA_HOME="/java-home"  
RUN set -ex; \  
\  
if [ -n "$APT_PROXY" ]; then echo "Acquire::http { Proxy
\"http://${APT_PROXY}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
if [ -n "$APT_PROXY_SSL" ]; then echo "Acquire::https { Proxy
\"https://${APT_PROXY_SSL}\"; };" > /etc/apt/apt.conf.d/00proxy; fi; \  
apt-get --yes update; \  
apt-get --yes install \  
openjdk-8-jdk=$JAVA_UBUNTU_VERSION \  
ca-certificates-java=$CA_CERTIFICATES_JAVA_VERSION \  
; \  
ln -sT "/usr/lib/jvm/java-8-openjdk-$(dpkg --print-architecture)" $JAVA_HOME;
\  
update-alternatives --get-selections | awk -v home="$(readlink -f $JAVA_HOME)"
'index($3, home) == 1 { $2 = "manual"; print | "update-alternatives --set-
selections" }'; \  
/var/lib/dpkg/info/ca-certificates-java.postinst configure; \  
\  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* /var/cache/apt/*; \  
rm -f /etc/apt/apt.conf.d/00proxy  
  
### METADATA
###################################################################  
ARG IMAGE  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
LABEL \  
org.label-schema.name=$IMAGE \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.schema-version="1.0"  

