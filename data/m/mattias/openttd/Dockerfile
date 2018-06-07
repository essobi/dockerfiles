FROM buildpack-deps:xenial-curl  
  
ARG OPENTTD_VERSION="1.7.1"  
ARG OPENGFX_VERSION="0.5.2"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libsdl1.2debian \  
libfontconfig1 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl --fail --silent --show-error --location
https://binaries.openttd.org/releases/${OPENTTD_VERSION}/openttd-${OPENTTD_VERSION}-linux-
generic-amd64.tar.gz \  
| tar -xzf - -C /opt \  
&& ln -fs /opt/openttd-${OPENTTD_VERSION}-linux-generic-amd64 /opt/openttd  
  
RUN curl --fail --silent --show-error --location
https://binaries.openttd.org/extra/opengfx/${OPENGFX_VERSION}/opengfx-${OPENGFX_VERSION}-all.zip
\  
| tar -xzf - -C /opt/openttd/baseset  
  
COPY ./entrypoint.sh /  
  
# Default port used by the game  
EXPOSE 3979/tcp  
EXPOSE 3979/udp  
# Advertise in server list  
EXPOSE 3978/udp  
  
VOLUME /root/.openttd  
  
ENTRYPOINT ["/entrypoint.sh"]  

