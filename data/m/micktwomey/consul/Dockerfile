FROM debian:7.8  
# Currently consul implicitly depends too much on gnu libc to work in these,
0.6 should be pure go.  
# When switched that should drop the docker image size down dramatically.  
# FROM progrium/busybox  
# FROM gliderlabs/alpine:3.1  
MAINTAINER Michael Twomey <mick@twomeylee.name>  
  
ENV CONSUL_VERSION 0.5.0  
# && apk add --update wget ca-certificates \  
# && opkg-install wget ca-certificates \  
RUN cd /tmp \  
&& apt-get update \  
&& apt-get install --yes wget ca-certificates unzip \  
&& wget
https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_linux_amd64.zip \  
&& unzip ${CONSUL_VERSION}_linux_amd64.zip \  
&& mv consul /usr/bin/consul \  
&& chmod 755 /usr/bin/consul \  
&& wget https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_web_ui.zip \  
&& unzip ${CONSUL_VERSION}_web_ui.zip \  
&& mkdir -p /consul/ui /consul/data /consul/config \  
&& mv dist/* /consul/ui \  
&& rm ${CONSUL_VERSION}_web_ui.zip dist/.gitkeep \  
&& rmdir dist \  
&& apt-get purge --yes wget unzip \  
&& apt-get autoremove --yes --purge \  
&& apt-get clean  
# Keep ca-certificates  
# && opkg-cl remove --autoremove wget ca-certificates || true  
# && apk del wget ca-certificates  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600  
VOLUME ["/consul/data"]  
  
ENTRYPOINT []  
CMD ["/usr/bin/consul", "agent", "-config-dir=/consul/config"]  
  
ADD ./config /consul/config  
ONBUILD ADD ./config /consul/config  

