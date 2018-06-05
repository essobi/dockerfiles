FROM debian:latest  
  
MAINTAINER Arne Schubert <atd.schubert@gmail.com>  
  
RUN set -x \  
&& apt-get update \  
&& DEBIAN_FRONTEND="noninteractive" apt-get install --no-install-recommends -y
git php5-cli php5-curl php5-sqlite ca-certificates zip tar bzip2 \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /in \  
&& mkdir -p /out \  
&& mkdir -p /build-init.d \  
&& useradd -ms /bin/bash bob \  
&& chown bob /in \  
&& chown bob /out  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENV MAPBENDER_REPOSITORY "https://github.com/mapbender/mapbender-starter.git"  
ENV MAPBENDER_BRANCH "release/3.0.6"  
ENV MAPBENDER_NAME "mapbender"  
ENV MAPBENDER_VERSION "3.0.6"  
ENV BUILD_NUMBER 1  
# bob the builder  
USER bob  
  
VOLUME ["out"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["build"]  

