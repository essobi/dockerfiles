FROM ubuntu:16.04  
MAINTAINER Patrick Kaiser <docker@pk.banovo.de>  
  
# Variables  
#
-----------------------------------------------------------------------------  
ENV CONTAINER_USER run  
ENV PATH "$PATH:/opt/strelaysrv/bin"  
ENV TZ "Europe/Berlin"  
# Copy binaries and entrypoint  
# Latest Release from
https://build.syncthing.net/job/strelaysrv/lastSuccessfulBuild/artifact/  
#
-----------------------------------------------------------------------------  
COPY sources/gosu-amd64 /usr/local/bin/gosu  
COPY sources/strelaysrv /opt/strelaysrv/bin/strelaysrv  
COPY docker-entrypoint.sh /usr/local/bin  
  
# Setup Container user  
# uid + guid will be changed on container startup on demand and set to values  
# defined in ENV vars  
#
-----------------------------------------------------------------------------  
RUN set -x \  
&& addgroup --gid 9001 ${CONTAINER_USER} \  
&& adduser --uid 9001 --gid 9001 --shell /bin/bash --home
/home/${CONTAINER_USER} \--gecos "" \--disabled-password ${CONTAINER_USER}  
  
# Base packages  
#
-----------------------------------------------------------------------------  
RUN set -x \  
&& chmod +x /usr/local/bin/gosu \  
&& chmod +x /opt/strelaysrv/bin/strelaysrv \  
&& chmod +x /usr/local/bin/docker-entrypoint.sh \  
&& gosu nobody true \  
&& mkdir -p /opt/strelaysrv/etc  
  
EXPOSE 22067  
EXPOSE 22070  
WORKDIR /opt/strelaysrv/bin  
  
CMD ["strelaysrv"]  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  

