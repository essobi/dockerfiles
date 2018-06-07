FROM debian  
  
LABEL MAINTAINER Emmanuel Gautier <docker@emmanuelgautier.fr>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV HUBIC_VERSION 2.1.0  
ENV HUBIC_VERSION_MINOR 53  
ENV HUBIC_PACKAGE_URL http://mir7.ovh.net/ovh-applications/hubic/hubiC-
Linux/${HUBIC_VERSION}/hubiC-
Linux-${HUBIC_VERSION}.${HUBIC_VERSION_MINOR}-linux.deb  
  
ENV HUBIC_EMAIL=your@email.ovh  
ENV HUBIC_PASSWORD=password  
  
RUN \  
apt-get update && \  
apt-get -y install \  
dbus \  
dbus-x11 \  
mono-runtime \  
libmono-sqlite4.0-cil \  
libmono-system-core4.0-cil \  
libmono-system-data4.0-cil \  
libmono-system-data-datasetextensions4.0-cil \  
libmono-system-drawing4.0-cil \  
libmono-system-runtime-serialization4.0-cil \  
libmono-system-xml-linq4.0-cil \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/ \  
&& \  
wget -O /tmp/hubiC.deb ${HUBIC_PACKAGE_URL} && \  
dpkg -i /tmp/hubiC.deb && \  
rm -v /tmp/hubiC.deb \  
&& mkdir -p /hubic  
  
VOLUME ["/hubic"]  
  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

