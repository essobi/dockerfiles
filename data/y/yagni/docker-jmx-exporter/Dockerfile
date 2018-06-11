FROM debian:8  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV JAVA_VERSION 8  
ENV JMX_PROMETHEUS_HTTPSERVER_VERSION 0.7-SNAPSHOT  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
DISTRO=debian && \  
CODENAME=jessie && \  
echo "deb http://http.debian.net/${DISTRO} ${CODENAME}-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install -yq --no-install-recommends \  
apt-utils \  
bash \  
curl \  
openjdk-${JAVA_VERSION}-jre-headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /jmx_prometheus_httpserver  
WORKDIR /jmx_prometheus_httpserver  
RUN curl -O -k -L https://github.com/yagniio/docker-jmx-
exporter/releases/download/$JMX_PROMETHEUS_HTTPSERVER_VERSION/jmx_prometheus_httpserver-$JMX_PROMETHEUS_HTTPSERVER_VERSION-
jar-with-dependencies.jar  
  
ADD docker-entrypoint.sh /jmx_prometheus_httpserver/docker-entrypoint.sh  
  
EXPOSE 9138  
VOLUME [ "/jmx_prometheus" ]  
  
ENTRYPOINT ["/jmx_prometheus_httpserver/docker-entrypoint.sh"]  
CMD [ "/jmx_prometheus/config.yml" ]

